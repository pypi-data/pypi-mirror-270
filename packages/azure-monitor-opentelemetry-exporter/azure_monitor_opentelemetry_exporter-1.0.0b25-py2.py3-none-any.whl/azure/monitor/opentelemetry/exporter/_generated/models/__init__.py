# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AvailabilityData
    from ._models_py3 import MessageData
    from ._models_py3 import MetricDataPoint
    from ._models_py3 import MetricsData
    from ._models_py3 import MonitorBase
    from ._models_py3 import MonitorDomain
    from ._models_py3 import PageViewData
    from ._models_py3 import PageViewPerfData
    from ._models_py3 import RemoteDependencyData
    from ._models_py3 import RequestData
    from ._models_py3 import StackFrame
    from ._models_py3 import TelemetryErrorDetails
    from ._models_py3 import TelemetryEventData
    from ._models_py3 import TelemetryExceptionData
    from ._models_py3 import TelemetryExceptionDetails
    from ._models_py3 import TelemetryItem
    from ._models_py3 import TrackResponse
except (SyntaxError, ImportError):
    from ._models import AvailabilityData  # type: ignore
    from ._models import MessageData  # type: ignore
    from ._models import MetricDataPoint  # type: ignore
    from ._models import MetricsData  # type: ignore
    from ._models import MonitorBase  # type: ignore
    from ._models import MonitorDomain  # type: ignore
    from ._models import PageViewData  # type: ignore
    from ._models import PageViewPerfData  # type: ignore
    from ._models import RemoteDependencyData  # type: ignore
    from ._models import RequestData  # type: ignore
    from ._models import StackFrame  # type: ignore
    from ._models import TelemetryErrorDetails  # type: ignore
    from ._models import TelemetryEventData  # type: ignore
    from ._models import TelemetryExceptionData  # type: ignore
    from ._models import TelemetryExceptionDetails  # type: ignore
    from ._models import TelemetryItem  # type: ignore
    from ._models import TrackResponse  # type: ignore

from ._azure_monitor_client_enums import (
    ContextTagKeys,
    DataPointType,
    SeverityLevel,
)

__all__ = [
    'AvailabilityData',
    'MessageData',
    'MetricDataPoint',
    'MetricsData',
    'MonitorBase',
    'MonitorDomain',
    'PageViewData',
    'PageViewPerfData',
    'RemoteDependencyData',
    'RequestData',
    'StackFrame',
    'TelemetryErrorDetails',
    'TelemetryEventData',
    'TelemetryExceptionData',
    'TelemetryExceptionDetails',
    'TelemetryItem',
    'TrackResponse',
    'ContextTagKeys',
    'DataPointType',
    'SeverityLevel',
]
