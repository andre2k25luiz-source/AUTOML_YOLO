# 🚀 AutoML YOLO (One-Shot Object Detection)

Sistema de **AutoML para Visão Computacional** capaz de treinar um modelo de detecção de objetos utilizando **apenas uma única imagem de entrada (one-shot)**.

O pipeline gera automaticamente um dataset sintético e treina um modelo baseado em **YOLOv8**.

---

## 🧠 Como funciona

O sistema segue o seguinte fluxo:

1. 📸 Usuário envia uma imagem com o objeto
2. ✂️ O objeto é recortado automaticamente
3. 🧩 O sistema gera imagens sintéticas (data synthesis)
4. 🏋️ O modelo YOLO é treinado automaticamente
5. 🔍 O modelo pode ser usado para detectar objetos em novas imagens

---

## 📁 Estrutura do Projeto

```
automl_yolo/
│
├── app.py                 # API Flask
├── generator.py           # Geração de dataset sintético
├── train.py               # Treinamento YOLO
├── predict.py             # Inferência
│
├── templates/
│   └── index.py           # Interface Streamlit
│
├── data/
│   ├── input/             # Imagem enviada pelo usuário
│   ├── backgrounds/       # Imagens de fundo
│   └── output/            # Dataset gerado
│
└── models/                # Modelos treinados
```

---

## ⚙️ Instalação

Clone o projeto e instale as dependências:

```bash
git clone <seu-repositorio>
cd automl_yolo

pip install -r requirements.txt
```

---

## ▶️ Como Executar

### 🔹 1. Iniciar a API (Flask)

```bash
python app.py
```

A API estará disponível em:

```
http://localhost:5000
```

---

### 🔹 2. Iniciar a Interface (Streamlit)

Em outro terminal:

```bash
streamlit run templates/index.py
```

---

## 📌 Pré-requisitos IMPORTANTES

Antes de treinar, você precisa adicionar imagens de fundo:

```
data/backgrounds/
```

Exemplo:

```
backgrounds/
├── bg1.jpg
├── bg2.jpg
├── bg3.jpg
```

⚠️ Sem isso o sistema não funciona.

---

## 📡 Endpoints da API

### 🔹 Treinar modelo

```
POST /train
```

**Body:**

* `image` (file)

**Descrição:**

* Gera dataset sintético
* Treina modelo automaticamente
* Salva em: `models/best.pt`

---

### 🔹 Fazer predição

```
POST /predict
```

**Body:**

* `image` (file)

**Retorno:**

* Bounding boxes detectadas

---

## 🏋️ Treinamento

O modelo utilizado é o **YOLOv8 (Ultralytics)**.

O sistema automaticamente:

* gera dataset sintético
* cria `data.yaml`
* executa o treinamento

---

## ⚠️ Limitações

* Segmentação simples (threshold)
* Sem sombras realistas
* Sem oclusão de objetos
* Pode não generalizar bem com poucos backgrounds

---

## 🚀 Melhorias Futuras

* Segmentação avançada com SAM
* Geração de dados com Stable Diffusion
* Multi-classe automática
* Sistema de cache de modelos
* Deploy em nuvem

---

## 💡 Objetivo

Este projeto demonstra como transformar:

👉 **1 imagem → dataset sintético → modelo funcional**

Utilizando conceitos modernos de:

* Data-centric AI
* Synthetic Data
* AutoML

---

## 📜 Licença

Este projeto é open-source e pode ser utilizado para fins educacionais e comerciais.

---

## 👨‍💻 Autor

Desenvolvido por André Luiz
