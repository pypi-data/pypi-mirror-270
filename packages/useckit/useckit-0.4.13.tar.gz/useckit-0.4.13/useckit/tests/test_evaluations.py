import os
import sys
import unittest

from useckit.paradigms.anomaly_detection.anomaly_paradigm import AnomalyParadigm
from useckit.paradigms.anomaly_detection.evaluation_methods.identification import \
    IdentificationOnly as AnomalyIdentification
from useckit.paradigms.anomaly_detection.evaluation_methods.identification_with_reject import \
    IdentificationWithReject as AnomalyIdentificationWithReject
from useckit.paradigms.anomaly_detection.evaluation_methods.verification import \
    Verification as AnomalyVerification
from useckit.paradigms.anomaly_detection.prediction_models.scikit_anomaly_prediction_model import \
    ScikitAnomalyPredictionModel
from useckit.paradigms.binary_verification.binary_verification_paradigm import BinaryVerificationParadigm
from useckit.paradigms.binary_verification.evaluation_methods.binary_verification_evaluation_method_scoring import \
    BinaryScoringVerification
from useckit.paradigms.binary_verification.prediction_models.verification_scikit_prediction_model import \
    VerificationSkLearnPredictionModel
from useckit.paradigms.distance_learning.distance_paradigm import DistanceMetricParadigm
from useckit.paradigms.distance_learning.evaluation_methods.identification import \
    IdentificationOnly as DistanceIdentification
from useckit.paradigms.distance_learning.evaluation_methods.identification_with_reject import \
    IdentificationWithReject as DistanceIdentificationWithReject
from useckit.paradigms.distance_learning.evaluation_methods.verification import \
    Verification as DistanceVerification
from useckit.paradigms.distance_learning.prediction_models.scikit_distance_model import ScikitDistancePredictionModel
from useckit.paradigms.time_series_classification.evaluation_methods.identification import \
    IdentificationOnly as TSCIdentification
from useckit.paradigms.time_series_classification.prediction_models.classification_scikit_prediction_model import \
    ClassificationScikitPredictionModel
from useckit.paradigms.time_series_classification.tsc_paradigm import TSCParadigm
from useckit.tests.test_utils import make_dataset, make_windowsliced_dataset

# resolves issues with gitlab runner
sys.setrecursionlimit(10000)
# disable gpu training for unittests
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


class TestUseckit(unittest.TestCase):

    def test_anomaly_prediction(self):
        data = make_dataset(shape=(100, 100), noisiness=0)
        encoder = AnomalyParadigm(verbose=True, prediction_model=ScikitAnomalyPredictionModel(),
                                  evaluation_methods=[AnomalyVerification(), AnomalyIdentification(),
                                                      AnomalyIdentificationWithReject()])
        encoder.evaluate(data)

    def test_time_series_classification(self):
        data = make_dataset(shape=(100, 100), noisiness=0)
        tsc = TSCParadigm(
            prediction_model=ClassificationScikitPredictionModel(),
            verbose=True, evaluation_methods=[TSCIdentification()])
        tsc.evaluate(data)

    def test_distance_metric(self):
        data = make_dataset(shape=(100, 100), noisiness=0)
        siamese = DistanceMetricParadigm(verbose=True, prediction_model=ScikitDistancePredictionModel(),
                                         evaluation_methods=[
                                             DistanceVerification(tradeoff_computation_speed_for_memory=True),
                                             DistanceIdentification(tradeoff_computation_speed_for_memory=True),
                                             DistanceIdentificationWithReject(
                                                 tradeoff_computation_speed_for_memory=True)])
        siamese.evaluate(data)
        siamese = DistanceMetricParadigm(verbose=True, prediction_model=ScikitDistancePredictionModel(),
                                         evaluation_methods=[
                                             DistanceVerification(tradeoff_computation_speed_for_memory=False),
                                             DistanceIdentification(tradeoff_computation_speed_for_memory=False),
                                             DistanceIdentificationWithReject(
                                                 tradeoff_computation_speed_for_memory=False)])
        siamese.evaluate(data)

    def test_anomaly_prediction_windowsliced(self):
        data = make_windowsliced_dataset(5, 10, shape=(20, 100), noisiness=0)
        encoder = AnomalyParadigm(verbose=True, prediction_model=ScikitAnomalyPredictionModel(),
                                  evaluation_methods=[AnomalyVerification(), AnomalyIdentification(),
                                                      AnomalyIdentificationWithReject()])
        encoder.evaluate(data)

    def test_time_series_classification_windowsliced(self):
        data = make_windowsliced_dataset(5, 10, shape=(20, 100), noisiness=0)
        tsc = TSCParadigm(
            prediction_model=ClassificationScikitPredictionModel(),
            verbose=True, evaluation_methods=[TSCIdentification()])
        tsc.evaluate(data)

    def test_distance_metric_windowsliced(self):
        data = make_windowsliced_dataset(5, 10, shape=(20, 100), noisiness=0)
        siamese = DistanceMetricParadigm(verbose=True, prediction_model=ScikitDistancePredictionModel(),
                                         evaluation_methods=[DistanceVerification(), DistanceIdentification(),
                                                             DistanceIdentificationWithReject()])
        siamese.evaluate(data)

    def test_binary_verification_ovr(self):
        # ovr = one vs rest case
        data = make_dataset(shape=(100, 100), noisiness=0)
        verif = BinaryVerificationParadigm(verbose=True,
                                           prediction_model=VerificationSkLearnPredictionModel(),
                                           evaluation_methods=[BinaryScoringVerification()],
                                           multiclass_classification_strategy='ovr')
        verif.evaluate(data)

    def test_binary_verification_ovo(self):
        # ovo = one vs one case
        data = make_dataset(shape=(100, 100), noisiness=0)
        verif = BinaryVerificationParadigm(verbose=True,
                                           prediction_model=VerificationSkLearnPredictionModel(),
                                           evaluation_methods=[BinaryScoringVerification()],
                                           multiclass_classification_strategy='ovo')
        verif.evaluate(data)

    def test_binary_verification_windowsliced(self):
        raise NotImplementedError("TODO: Implement unittests for test_binary_verification_ovr() and "
                                  "test_binary_verification_ovo() with windowslicing dataset.")


if __name__ == '__main__':
    unittest.main()
