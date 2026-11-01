# F1 Podium Predictor — São Paulo GP 2026

Projeto de Machine Learning para estimar a probabilidade de cada piloto terminar no pódio.

**Criador:** Code & Context | **Status:** Em desenvolvimento

## Objetivo
Pipeline reproduzível de coleta, tratamento, engenharia de atributos, treinamento e avaliação.

## Estrutura
- `data/raw/`: dados originais
- `data/processed/`: bases tratadas
- `notebooks/`: análises e experimentos
- `src/f1_predictor/`: código Python organizado em módulos
- `models/`: modelos treinados
- `reports/figures/`: gráficos exportados
- `tests/`: testes automatizados

## Instalação
Recomendado Python 3.11 ou 3.12.

```bash
python -m venv .venv
.venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
pip install -e .
```

## Coletar uma corrida
```bash
python -m f1_predictor.data.collect --year 2025 --gp Brazil --session R
```

## Metodologia
- Unidade inicial: piloto por corrida.
- Alvo: `podium` (posição final entre 1º e 3º).
- Validação cronológica por corrida/temporada.
- Usar somente atributos disponíveis antes da corrida prevista.
- Métricas: precision, recall, F1 e Brier score; comparar com baseline.

## Fontes
- [FastF1](https://docs.fastf1.dev/)
- [Jolpica-F1](https://github.com/jolpica/jolpica-f1)

Não versionar grandes bases de terceiros nem redistribuir dados sem verificar seus termos de uso. Previsões são experimentais, não garantias.

Este repositório integra os projetos do canal **Code & Context**.
