# ---------------------------------------------------------------------
# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
from dataclasses import dataclass
from functools import cached_property
from typing import Any, Dict, List, Optional, Type, Union, cast

import qai_hub as hub

from qai_hub_models.models.common import TargetRuntime
from qai_hub_models.utils.config_loaders import QAIHMModelCodeGen, QAIHMModelInfo
from qai_hub_models.utils.scorecard.common import (
    REFERENCE_DEVICE_PER_SUPPORTED_CHIPSETS,
    SCORECARD_DEVICE_NAME_TO_CHIPSET_NAME,
)


@dataclass
class JobSummary:
    model_id: str
    job_id: Optional[str]
    runtime: TargetRuntime

    def __post_init__(self):
        assert self.model_id
        assert self.runtime
        # Verify Job Exists
        if self.job_id:
            assert self.job

    @classmethod
    def from_model_id(
        cls: Type["JobSummary"], model_id: str, job_ids: Dict[str, str]
    ) -> List:
        """
        Reads jobs for `model_id` from the dictionary and creates summaries for each. `job_ids` format:
        Either:
            <model_id>|<runtime>|<device>|<model_component_id> : job_id
            <model_id>|<runtime>|<device> : job_id

        Returns models in this format:
            model_id: List[Summary]
        """
        raise NotImplementedError()

    @cached_property
    def job(self) -> Optional[hub.Job]:
        """Get the hub.CompileJob object."""
        if not self.job_id:
            return None

        job = hub.get_job(self.job_id)
        job.wait()
        return job

    @cached_property
    def skipped(self) -> bool:
        return self.job_id is None

    @cached_property
    def failed(self) -> bool:
        return self._job_status and self._job_status.failure  # type: ignore

    @cached_property
    def success(self) -> bool:
        return self._job_status and self._job_status.success  # type: ignore

    @cached_property
    def status_message(self) -> str:
        return "Skipped" if self.skipped else self._job_status.message  # type: ignore

    @cached_property
    def _job_status(self) -> Optional[hub.JobStatus]:
        """Get the job status of the profile job."""
        if not self.skipped:
            return self.job.get_status()  # type: ignore
        return None

    @cached_property
    def job_status(self) -> str:
        """Get the job status of the profile job."""
        if not self.skipped:
            if self._job_status.success:  # type: ignore
                return "Passed"
            elif self._job_status.failure:  # type: ignore
                return "Failed"
        return "Skipped"

    @cached_property
    def quantized(self) -> str:
        """Quantized models are marked so precision can be correctly recorded."""
        return (
            "Yes"
            if self.model_id.endswith("Quantized")
            or self.model_id.endswith("Quantizable")
            else "No"
        )


@dataclass
class CompileJobSummary(JobSummary):
    @classmethod
    def from_model_id(
        cls: Type["CompileJobSummary"], model_id: str, job_ids: Dict[str, str]
    ) -> List["CompileJobSummary"]:
        """
        Reads jobs for `model_id` from the dictionary and creates summaries for each. `job_ids` format:
        Either:
            <model_id>|<runtime>|<device>|<model_component_id> : job_id
            <model_id>|<runtime>|<device> : job_id

        Returns models in this format:
            model_id: List[Summary]
        """
        model_info = QAIHMModelInfo.from_model(model_id)
        model_code_gen: QAIHMModelCodeGen = model_info.code_gen_config
        model_runs = []
        components = []

        if model_code_gen.components:
            if model_code_gen.default_components:
                components = model_code_gen.default_components
            else:
                components = list(model_code_gen.components.keys())

        for runtime in TargetRuntime:
            if not components:
                model_runs.append(
                    cls(
                        model_id=model_info.name,
                        job_id=job_ids.get(f"{model_id}_{runtime.name}", None),
                        runtime=runtime,
                    )
                )
            else:
                for component in components:
                    model_runs.append(
                        cls(
                            model_id=component,
                            job_id=job_ids.get(
                                f"{model_id}_{runtime.name}_{component}", None
                            ),
                            runtime=runtime,
                        )
                    )

        return model_runs

    def __post_init__(self):
        super().__post_init__()
        if not self.skipped:
            assert isinstance(self.job, hub.CompileJob)

    @cached_property
    def compile_job(self) -> Optional[hub.CompileJob]:
        """Get the hub.CompileJob object."""
        if self.job:
            return None
        return cast(hub.CompileJob, self.job)


@dataclass
class ProfileJobSummary(JobSummary):
    _chipset: str

    @classmethod
    def from_model_id(
        cls: Type["ProfileJobSummary"], model_id: str, job_ids: Dict[str, str]
    ) -> List["ProfileJobSummary"]:
        """
        Reads jobs for `model_id` from the dictionary and creates summaries for each. `job_ids` format:
        Either:
            <model_id>|<runtime>|<device>|<model_component_id> : job_id
            <model_id>|<runtime>|<device> : job_id

        Returns models in this format:
            model_id: List[Summary]
        """
        model_info = QAIHMModelInfo.from_model(model_id)
        model_code_gen: QAIHMModelCodeGen = model_info.code_gen_config
        model_runs = []
        components = []

        if model_code_gen.components:
            if model_code_gen.default_components:
                components = model_code_gen.default_components
            else:
                components = list(model_code_gen.components.keys())

        for runtime in TargetRuntime:
            for device, chipset in SCORECARD_DEVICE_NAME_TO_CHIPSET_NAME.items():
                run_dev = f"{runtime.name}-{device}"
                if not components:
                    if (job_id := job_ids.get(f"{model_id}_{run_dev}", None)) is None:
                        continue
                    model_runs.append(
                        cls(
                            model_id=model_info.name,
                            job_id=job_id,
                            runtime=runtime,
                            _chipset=chipset,
                        )
                    )
                else:
                    for component in components:
                        if (
                            job_id := job_ids.get(
                                f"{model_id}_{run_dev}_{component}", None
                            )
                        ) is None:
                            continue
                        model_runs.append(
                            cls(
                                model_id=component,
                                job_id=job_id,
                                runtime=runtime,
                                _chipset=chipset,
                            )
                        )

        return model_runs

    def __post_init__(self):
        super().__post_init__()
        assert self.chipset in REFERENCE_DEVICE_PER_SUPPORTED_CHIPSETS
        if not self.skipped:
            assert isinstance(self.job, hub.ProfileJob)
            if self._job_status.success:
                assert self.profile_results

    @cached_property
    def chipset(self) -> str:
        """Chipset the job was run on."""
        if not self.job:
            return self._chipset

        hub_device = self.job.device
        for attr in hub_device.attributes:
            if attr.startswith("chipset:"):
                return attr.split(":")[1]
        raise ValueError("No chipset found.")

    @cached_property
    def device(self) -> hub.Device:
        return (
            self.job.device
            if self.job
            else REFERENCE_DEVICE_PER_SUPPORTED_CHIPSETS[self.chipset]
        )

    @cached_property
    def profile_job(self) -> Optional[hub.ProfileJob]:
        """Get the hub.CompileJob object."""
        if not self.job:
            return None
        return cast(hub.ProfileJob, self.job)

    @cached_property
    def profile_results(self) -> Optional[Dict[str, Any]]:
        """Profile results from profile job."""
        if self.job_status == "Passed":
            return self.profile_job.download_profile()  # type: ignore
        return None

    @cached_property
    def inference_time(self) -> Union[float, str]:
        """Get the inference time from the profile job."""
        if self.profile_results is not None:
            return float(
                self.profile_results["execution_summary"]["estimated_inference_time"]
            )
        return "null"

    @cached_property
    def throughput(self) -> Union[float, str]:
        """Get the throughput from the profile job."""
        if not isinstance(self.inference_time, str):
            return 1000000 / self.inference_time  # type: ignore
        return "null"

    def get_layer_info(self, unit: str) -> int:
        """Count layers per compute unit."""
        if self.profile_results is not None:
            count: int = 0
            count = sum(
                1
                for detail in self.profile_results["execution_detail"]
                if detail["compute_unit"] == unit
            )
            return count
        return 0

    @cached_property
    def npu(self) -> Any:
        """Get number of layers running on NPU."""
        return self.get_layer_info("NPU") if self.profile_results is not None else 0

    @cached_property
    def gpu(self) -> Any:
        """Get number of layers running on GPU."""
        return self.get_layer_info("GPU") if self.profile_results is not None else 0

    @cached_property
    def cpu(self) -> Any:
        """Get number of layers running on CPU."""
        return self.get_layer_info("CPU") if self.profile_results is not None else 0

    @cached_property
    def total(self) -> Any:
        """Get the total number of layers."""
        return self.npu + self.gpu + self.cpu

    @cached_property
    def primary_compute_unit(self) -> str:
        """Get the primary compute unit."""
        layers_npu = self.npu
        layers_gpu = self.gpu
        layers_cpu = self.cpu

        if layers_npu == 0 and layers_gpu == 0 and layers_cpu == 0:
            return "null"
        compute_unit_for_most_layers = max(layers_cpu, layers_gpu, layers_npu)
        if compute_unit_for_most_layers == layers_npu:
            return "NPU"
        elif compute_unit_for_most_layers == layers_gpu:
            return "GPU"
        return "CPU"

    @cached_property
    def peak_memory_range(self) -> Dict[str, int]:
        """Get the estimated peak memory range."""
        if self.profile_results is not None:
            low, high = self.profile_results["execution_summary"][
                "inference_memory_peak_range"
            ]
            return dict(min=low, max=high)
        return dict(min=0, max=0)

    @cached_property
    def precision(self) -> str:
        """Get the precision of the model based on the run."""
        if self.profile_results is not None:
            compute_unit = self.primary_compute_unit
            if compute_unit == "CPU":
                return "fp32"
            if self.quantized == "Yes":
                return "int8"
            return "fp16"
        return "null"

    @cached_property
    def performance_metrics(self) -> Dict[str, Any]:
        return dict(
            inference_time=self.inference_time,
            throughput=self.throughput,
            estimated_peak_memory_range=self.peak_memory_range,
            primary_compute_unit=self.primary_compute_unit,
            precision=self.precision,
            layer_info=dict(
                layers_on_npu=self.npu,
                layers_on_gpu=self.gpu,
                layers_on_cpu=self.cpu,
                total_layers=self.total,
            ),
            job_id=self.job_id,
            job_status=self.job_status,
        )
