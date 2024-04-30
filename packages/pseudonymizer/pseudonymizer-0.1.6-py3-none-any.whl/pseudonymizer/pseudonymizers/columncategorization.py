from pseudonymizer.pseudonymizer import Pseudonymizer
import pandas as pd

class CategorizationOfColumn(Pseudonymizer):
    """수치(연속형) 데이터를 임의의 수를 기준으로 범위(범주형)으로 설정하는 가명처리기법 구체클래스
    
       Parameters
       ----------
       numeric_type : bin or pct
       grouping_standard : 숫자 또는 리스트
       right : 폐구간의 경우 True, 개구간의 경우 False
       ascending : 오름차순의 경우 True, 내림차순의 경우 

       Examples
       --------
       repayment_risk_pseudo = CategorizationOfColumn(numeric_type="pct", grouping_standard=5, 
                                                      right=False, ascending=True)
    """
    def __init__(self, numeric_type: str, grouping_standard, right: bool, ascending: bool):
        self.numeric_type = numeric_type
        self.grouping_standard = grouping_standard
        self.right = right
        self.ascending = ascending
    
    def pseudonymizeData(self, dataseries):
        """식별성이 높은 그룹을 하나로 묶는 메서드"""
        if self.numeric_type == "bin":
            return self.pseudonymizeAmountbyBin(dataseries, self.grouping_standard, self.right, self.ascending)
        elif self.numeric_type == "pct":
            return self.pseudonymizeAmountbyPct(dataseries, self.grouping_standard, self.right, self.ascending)        
        else: 
            raise ValueError(f"{self.numeric_type}은 유효한 범주화 기법 적용 유형이 아닙니다.")

    def makeLabels(self, num_type, dataseries, grouping_standard, ascending: bool):
        """범주화 중 필요한 label을 만들어주는 클래스"""
        if num_type == "pct":
            labels = []
            if isinstance(grouping_standard, int):
                return [f"{i} 이상" for i in range(0, 100, grouping_standard)]
            else:
                for i in range(len(grouping_standard)):
                    if i == 0:
                        label = f"{grouping_standard[i]} 미만"
                        labels.append(label)
                    elif 0 < i < len(grouping_standard) - 1:
                        label = f"{grouping_standard[i-1]} ~ {grouping_standard[i]}"
                        labels.append(label)
                    else:
                        label1 = f"{grouping_standard[i-1]} ~ {grouping_standard[i]}"
                        labels.append(label1)
                        label2 = f"{grouping_standard[i]} 이상"
                        labels.append(label2)

                if ascending == False:
                    labels.reverse()
                return labels

        elif num_type == "bin":
            labels = []
            if isinstance(grouping_standard, int):
                bins = pd.cut(dataseries, bins=grouping_standard).unique()
                for category in bins:
                    start_value = category.left
                    end_value = category.right
                    labels.append(f"{start_value} ~ {end_value}")
            else:
                category_values = pd.cut(dataseries, bins=grouping_standard).value_counts(sort=False)
                for category in list(category_values.index):
                    start_value = category.left
                    end_value = category.right
                    labels.append(f"{start_value} ~ {end_value}")

            if ascending == False:
                labels.reverse()
            return labels

        else:
            raise ValueError(f"{num_type}은 유효한 범주화 기법 적용 유형이 아닙니다.")

    def pseudonymizeAmountbyBin(self, dataseries, grouping_standard, right: bool, ascending: bool):
        """기타 금액 구간별 범주화 메서드
        신용공여금액(예: 한도/건별대출, 담보대출, 리스/카드할부금융서비스 등)의 일정 급간화
        pd.cut 활용하여 범주화하되, 입력값 및 오름차순/내림차순, 급간 선택에 따라 파라미터를 달리함
        """
        if isinstance(grouping_standard, list):
            num = len(grouping_standard)
            data = pd.cut(dataseries, bins = num, labels = grouping_standard, right = right)
            return data

        elif isinstance(grouping_standard, int):
            labels = self.makeLabels("bin", dataseries, grouping_standard, ascending = ascending)                              
            data = pd.cut(dataseries, bins = grouping_standard, labels = labels, right = right)
            return data

        else:
            raise ValueError("grouping_standard는 list 또는 int 타입으로 입력해 주십시오.")
            
    def pseudonymizeAmountbyPct(self, dataseries, grouping_standard, right: bool, ascending: bool):
        """기타 금액 백분위에 의한 범주화 메서드
        개인사업자의 추청매출액/평당월임대료를 백분위수에 따라 매출등급화(90~100%, 65~90%, 35~65%, 10~35%, 0~10%)

        - 각 레코드별 등수 구하기 (중복값은 가장 낮은 순위로)
        - 백분위수 = ((등수 - 1) / 컬럼 레코드 갯수) * 100
        - 백분위수별로 pd.cut
        """
        rank_dataseries = dataseries.copy()
        rank_dataseries["rank"] = rank_dataseries.rank(method='min')

        percentiles = []
        for rank in rank_dataseries["rank"]:
            percentile = ((rank - 1) / len(rank_dataseries['rank'])) * 100
            percentiles.append(percentile)
        rank_dataseries["percentile"] = percentiles
        new_labels = self.makeLabels("pct", rank_dataseries, grouping_standard, ascending)

        if isinstance(grouping_standard, int):
            # 디버깅 파트(int 타입에 안맞게 len(grouping_standard)로 발생하는 오류)
            bins = [0] + list(range(100, 0, -grouping_standard))[::-1] + [100]
        else:
            # 중복된 값을 제거하고 정렬
            unique_sorted_bins = sorted(set(grouping_standard))
            bins = [0] + unique_sorted_bins + [100]

        result_dataseries = pd.cut(rank_dataseries["percentile"], bins=bins, labels=new_labels, right=right, duplicates="drop")
        return result_dataseries