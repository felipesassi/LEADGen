import pandas as pd
import numpy as np

class Keep_Features():
    def __init__(self, features):
        self.features = features
        
    def fit(self, x, y=None):
        pass
    
    def transform(self, x, y=None):
        if self.features == "all":
            return x
        else:
            return x[self.features]
    
    def fit_transform(self, x, y=None):
        x = self.transform(x)
        return x

class Remove_NaN_Data():
    def __init__(self):
        pass
    
    def fit(self, x, y=None):
        pass
    
    def transform(self, x, y=None):
        x['qt_socios_st_regular'] = x['qt_socios_st_regular'].fillna(0)
        x['idade_media_socios'] = x['idade_media_socios'].fillna(0)
        x['idade_maxima_socios'] = x['idade_maxima_socios'].fillna(0)
        x['idade_minima_socios'] = x['idade_minima_socios'].fillna(0)
        x['empsetorcensitariofaixarendapopulacao'] = x['empsetorcensitariofaixarendapopulacao'].fillna(0)
        x['qt_socios_pf'] = x['qt_socios_pf'].fillna(0) 
        x['qt_socios_pj'] = x['qt_socios_pj'].fillna(0)
        x['qt_socios'] = x['qt_socios'].fillna(0)
        x['fl_optante_simples'] = x['fl_optante_simples'].fillna(True)
        x['fl_optante_simei'] = x['fl_optante_simei'].fillna(True)
        x['nm_meso_regiao'] = x['nm_meso_regiao'].fillna("OUTROS")
        x['nm_micro_regiao'] = x['nm_micro_regiao'].fillna("OUTROS")
        x['nu_meses_rescencia'] = x['nu_meses_rescencia'].fillna(0)
        x['de_faixa_faturamento_estimado_grupo'] = x['de_faixa_faturamento_estimado_grupo'].fillna("OUTROS")
        x['vl_faturamento_estimado_aux'] = x['vl_faturamento_estimado_aux'].fillna(0)
        x['vl_faturamento_estimado_grupo_aux'] = x['vl_faturamento_estimado_grupo_aux'].fillna(0)
        x['de_faixa_faturamento_estimado'] = x['de_faixa_faturamento_estimado'].fillna("SEM INFORMACAO")
        x['de_saude_rescencia'] = x['de_saude_rescencia'].fillna("SEM INFORMACAO")
        x['de_saude_tributaria'] = x['de_saude_tributaria'].fillna("SEM INFORMAÇÃO")
        x['de_nivel_atividade'] = x['de_nivel_atividade'].fillna("OUTROS")
        x['sg_uf_matriz'] = x['sg_uf_matriz'].fillna("OUTROS")
        x['fl_simples_irregular'] = x['fl_simples_irregular'].fillna(True)
        return x
    
    def fit_transform(self, x, y=None):
        x = self.transform(x)
        return x

if __name__ == "__main__":
    pass