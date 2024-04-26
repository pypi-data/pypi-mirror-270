from .bounding_box_metrics_collector import BoundingBoxMetricsCollector as BoundingBoxMetricsCollector, COCOAnnotation as COCOAnnotation, COCOGroundTruth as COCOGroundTruth, COCOPrediction as COCOPrediction
from .classification_metrics_collector import ClassificationMetricsCollector as ClassificationMetricsCollector
from .embeddings_metrics_collector import EmbeddingsMetricsCollector as EmbeddingsMetricsCollector
from .functional_metrics_collector import FunctionalMetricsCollector as FunctionalMetricsCollector
from .metrics_collector_base import MetricsCollector as MetricsCollector
from .segmentation_metrics_collector import SegmentationMetricsCollector as SegmentationMetricsCollector
from tlc.client.torch.metrics.predictor import PredictorOutput as PredictorOutput
from tlc.core.builtins.types import MetricData as MetricData, SampleData as SampleData
from typing import Callable

MetricsCollectorCallableType = Callable[[SampleData, PredictorOutput], dict[str, MetricData]]
MetricsCollectorType = list[MetricsCollector] | MetricsCollector | list[MetricsCollectorCallableType] | MetricsCollectorCallableType
