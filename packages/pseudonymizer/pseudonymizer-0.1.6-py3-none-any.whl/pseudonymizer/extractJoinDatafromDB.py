from pseudonymizer.cryptocontainers.DBContainer import DBContainer
from pseudonymizer.encryptionPseudonyms.pyMySQLQuery import PyMySQLQuery


class ExtractJoinDatafromDB(PyMySQLQuery):
    """가명정보집합물 반출 클래스
    
       Parameters
       ----------
       external_data : 최종 결합 결과 테이블과 함께 반출하려는 기준 테이블명 
       pw, serverIP, port_num, user_name, kr_encoder : DB 접속 비밀번호, IP, 포트명, 유저명, 인코더 명
       database_name : 연결 대상 DB 스키마 이름

       Examples
       --------
       extract_data = ExtractJoinDatafromDB(external_data="FINANCE_TARGET", 
                                            pw = "1234", serverIP = "localhost", port_num = 3306, user_name = "root", 
                                            database_name = "FINANCIALCONSUMER", kr_encoder = "utf8")
    """
    def __init__(self, external_data: str, pw: str, serverIP: str, port_num: int, user_name: str, database_name: str, kr_encoder: str):
        self.external_data = external_data 
        # [external_data] TargetTable_i or None 
        super().__init__(pw = pw)
        super().connectDatabase(serverIP, port_num, user_name, database_name, kr_encoder)
    
    def extractCombineData(self, combine_schema, combine_tablename):
        """가명결합 완료된 내부결합 정보집합물을 반환하는 실행 메서드"""
        COMBINE_SELECT_DQL = f"SELECT * FROM {combine_schema}.{combine_tablename}"
        super().dataQueryLanguage(COMBINE_SELECT_DQL)
        self.table = super().executeQueryAsDataFrame()
        super().commitTransaction()

    def extractcreateLeftOuterJoinData(self, outer_schema: str, outer_tablename: str, 
                                       target_schema: str, target_tablename: str, 
                                       combine_schema: str, combine_tablename: str, serialnum_column: str):
        """가명결합 시 제외된 결합대상정보를 반환하는 실행 메서드
        
           Parameters
           ----------
           outer_schema, outer_tablename : 가명결합 제외대상 스키마, 테이블명
           target_schema, target_tablename : 원본 결합대상정보 스키마, 테이블명
           combine_schema, combine_tablename : 결합 완료 스키마, 테이블명
           serialnum_column : 일련번호 컬럼명
        
           Examples
           --------
           extract_data.extractcreateLeftOuterJoinData(outer_schema="FINANCIALCONSUMER", outer_tablename="FINANCE_JOINED",
                                                       target_schema="FINANCIALCONSUMER", target_tablename="FINANCE_TARGET",
                                                       combine_schema="FINANCIALCONSUMER", combine_tablename="FINANCE_RETAIL_TARGETS",
                                                       serialnum_column="SERIALNUM_FINANCE")
        
        """
        self.createLeftOuterJoinData(outer_schema, outer_tablename, target_schema, target_tablename, combine_schema, combine_tablename, serialnum_column)
        OUTER_SELECT_DQL = f"SELECT * FROM {outer_schema}.{outer_tablename}"
        super().dataQueryLanguage(OUTER_SELECT_DQL)
        self.table = super().executeQueryAsDataFrame()
        super().commitTransaction()

    def createLeftOuterJoinData(self, outer_schema: str, outer_tablename: str, 
                                target_schema: str, target_tablename: str, 
                                combine_schema: str, combine_tablename: str, serialnum_column: str):
        """가명결합 정보집합물에서 제외된 나머지 결합대상정보를 추출하여 테이블을 생성하는 메서드
        
           Parameters
           ----------
           outer_schema, outer_tablename : 가명결합 제외대상 스키마, 테이블명
           target_schema, target_tablename : 원본 결합대상정보 스키마, 테이블명
           combine_schema, combine_tablename : 결합 완료 스키마, 테이블명
           serialnum_column : 일련번호 컬럼명
        """
        schema, tablename = self.addOuterTable(outer_schema, outer_tablename)
        create_table_sql = f"CREATE TABLE {schema}.{tablename} AS SELECT "
        leftouter_join_dql = f"FROM {combine_schema}.{combine_tablename} LEFT OUTER JOIN {target_schema}.{target_tablename} ON {target_schema}.{target_tablename}.{serialnum_column} = {combine_schema}.{combine_tablename}.{serialnum_column}"
        
        join_columns = []

        target_columns = self.returnTablesColumns(target_schema, target_tablename)
        for column in target_columns:
            if column == serialnum_column:
                join_columns.append(f"{target_schema}.{target_tablename}.{column} AS {column}_TARGET")
            else:
                join_columns.append(f"{target_schema}.{target_tablename}.{column}")

        combine_columns = self.returnTablesColumns(combine_schema, combine_tablename)
        for column in combine_columns:
            if column == serialnum_column:
                join_columns.append(f"{combine_schema}.{combine_tablename}.{column} AS {column}_COMBINE")
            else:
                join_columns.append(f"{combine_schema}.{combine_tablename}.{column}")

        column_names_sql = ', '.join(join_columns)

        data_query_language = create_table_sql + column_names_sql + " " + leftouter_join_dql

        super().dataQueryLanguage(data_query_language)
        super().executeQuery()
        super().commitTransaction()

    @classmethod
    def addOuterTable(cls, schema, tablename):
        """가명결합 시 제외되는 LEFT OUTER JOIN 결합대상정보 스키마, 테이블명을 선언하는 클래스 메서드"""
        cls.combine_table = DBContainer()
        cls.combine_table.setSchemaTable(schema, tablename)
        schema = cls.combine_table.getSchema()
        tablename = cls.combine_table.getTable()
        return schema, tablename
    
    def returnTablesColumns(self, schema: str, tablename: str):
        """테이블 컬럼명 확인절차 및 반환 실행 메서드"""
        sql = f"SHOW COLUMNS FROM {schema}.{tablename}"
        super().dataQueryLanguage(sql)
        targettable_columns = super().executeQueryAsDataFrame()["Field"].tolist()
        return targettable_columns