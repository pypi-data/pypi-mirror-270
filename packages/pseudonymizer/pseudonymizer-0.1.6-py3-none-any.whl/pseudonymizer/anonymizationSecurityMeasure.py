from pseudonymizer.pseudonym import Pseudonym
from collections import Counter
import numpy as np


class AnonymizationSecurityMeasure(Pseudonym):
    """익명처리 기법이 적용된 정보의 안전성을 측정하는 지표"""
    def __init__(self, dataframe, attributes, anonymizeddata, degreeoffreedom):
        super().__init__(dataframe)
        super().categorizeEquivalentClass(attributes)
        self.anonymizeddata = anonymizeddata
        self.degreeoffreedom = degreeoffreedom
        
    def __str__(self):
        """캡슐화된 데이터셋의 동질집합 유형을 반환하는 메서드"""
        return self.equivalent_class.keys()

    def measureSecurity(self, parameter, quasi_identifiers, sensitive_attribute):
        """
        데이터의 안전성을 측정하는 메서드
        """
        index_list = self.equivalent_class[quasi_identifiers]
        column_reference = self._dataframe.columns.get_loc(sensitive_attribute)
        column_forward = self.anonymizeddata.columns.get_loc(sensitive_attribute)

        if parameter == "var":
            variance_reference = self.meanDistributionECMetric(self._dataframe.iloc[index_list, column_reference])
            variance_forward = self.meanDistributionECMetric(self.anonymizeddata.iloc[index_list, column_forward])
            return variance_reference, variance_forward
        
        elif parameter == "norm_aver":
            average_reference = self.normalizedAverageECSizeMetric(self._dataframe.iloc[index_list, column_reference])
            average_forward = self.normalizedAverageECSizeMetric(self.anonymizeddata.iloc[index_list, column_forward])
            return average_reference, average_forward
        
        elif parameter == "entropy":
            entropy_reference = self.nonUniformEntropyMetric(self._dataframe.iloc[index_list, column_reference])
            entropy_forward = self.nonUniformEntropyMetric(self.anonymizeddata.iloc[index_list, column_forward])
            return entropy_reference, entropy_forward
        
        else:
            raise ValueError(f"{parameter}은(는) 유효한 익명정보 안전성 평가지표가 아닙니다.")
            
    # @classmethod
    def meanDistributionECMetric(self, X):
        """동질집합별 속성들에 대한 평균 분포도(분산) 계산 메서드"""
        if self.degreeoffreedom == 0:  
            # 클래스 변수로 접근
            # 표본분산
            variance_X = np.mean(abs(X - np.mean(X))**2)
        elif self.degreeoffreedom == 1:
            # 불편분산(불편추정량)
            variance_X = sum((x - np.mean(x))**2 for x in X) / (len(X) - 1)
        else:
            raise ValueError(f"{self.degreeoffreedom}은(는) 유효한 자유도가 아닙니다.")
        return variance_X

    @classmethod
    def normalizedAverageECSizeMetric(cls, X):
        """정규화된 동질집합들의 평균 크기 계산 메서드(0과 1 사이로 데이터 범위 조정))"""
        normalized_values = (X - min(X)) / (max(X) - min(X))
        normalized_average = sum(normalized_values) / len(X)
        return normalized_average

    @classmethod
    def nonUniformEntropyMetric(cls, X):
        """비균일 엔트로피 방법을 이용한 K익명성 프라이버시 보호 모델에서의 정보 손실 측도"""
        prob_distribution = []
        prob_distribution = [len(x) / len(X) for x in Counter(X).items()]
        class_entropy = []

        for p in prob_distribution:
            if p != 0:
                class_entropy.append(np.log(p)*p)
        
        return sum(class_entropy)
