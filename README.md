# Detecção de emoções em tempo real
## 
- Este projeto visa detectar emoções humanas em tempo real utilizando uma câmera de vídeo. Ele utiliza técnicas de visão computacional e aprendizado de máquina para identificar rostos e classificar as emoções expressas neles. O modelo é baseado em uma rede neural treinada para classificar 7 emoções principais.

## Tabela de Conteúdos

- [Detecção de emoções em tempo real](#detecção-de-emoções-em-tempo-real)
  - [](#)
  - [Tabela de Conteúdos](#tabela-de-conteúdos)
  - [Descrição do Projeto](#descrição-do-projeto)
  - [Funcionalidades](#funcionalidades)
  - [Estrutura do Projeto](#estrutura-do-projeto)
    - [Modelos](#modelos)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Uso](#uso)
    - [Parâmetros de Configuração](#parâmetros-de-configuração)
  - [Contribuição](#contribuição)
  - [Licença](#licença)
  - [](#-1)

## Descrição do Projeto

Este projeto utiliza o modelo `model_frontalface_emotion.h5` para detectar emoções faciais em tempo real, capturando vídeos da webcam. O projeto é modularizado e pode ser facilmente adaptado para diferentes fontes de vídeo ou modelos de detecção de emoções.

O modelo foi treinado para classificar as seguintes emoções:
- Raiva
- Nojo
- Medo
- Felicidade
- Tristeza
- Surpresa
- Neutro

## Funcionalidades

- Detecção de rostos utilizando o classificador Haar Cascade.
- Classificação de emoções em rostos detectados.
- Exibição do vídeo com a emoção detectada sobre cada rosto.
- Interface simples para exibição e controle do processo (pressione "Q" para sair).
  
## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
emotion_detection/
│
├── config.py                # Configurações do projeto (caminhos dos modelos e labels)
├── main.py                  # Ponto de entrada do programa
├── core/
│   ├── video_capture.py     # Classe para captura de vídeo
│   ├── model_manager.py     # Gerenciador de modelos de detecção
│   └── emotion_processor.py # Processamento das emoções
└── utils/
    └── helpers.py           # Funções auxiliares
```

### Modelos

Os modelos necessários para a execução do projeto são:
- **Modelo de detecção facial**: `frontalface_emotion.xml`
- **Modelo de classificação de emoções**: `model_frontalface_emotion.h5`

Esses modelos devem ser colocados na pasta `models/` ou em um diretório de sua escolha, e seus caminhos devem ser configurados no arquivo `config.py`.

## Pré-requisitos

Antes de rodar o projeto, você precisa garantir que tem os seguintes pacotes instalados:

- Python 3.x
- OpenCV
- TensorFlow
- NumPy

Você pode instalar as dependências com o seguinte comando:

```bash
pip install opencv-python tensorflow numpy
```

Além disso, você precisará do arquivo `haarcascade_frontalface_default.xml` (classificador Haar para detecção de rostos) e do modelo treinado `model_frontalface_emotion.h5`. Ambos podem ser encontrados no repositório ou fornecidos como parte do projeto.

## Instalação

1. Clone o repositório ou baixe os arquivos:

```bash
git clone https://github.com/raulbatalha/emotion_detection.git
```

2. Navegue até o diretório do projeto:

```bash
cd emotion_detection
```

3. Crie um ambiente virtual para o projeto:

```bash
python -m venv envemotion
```

4. Ative o ambiente virtual:
   - No **Windows**:
     ```bash
     .\envemotion\Scripts\activate
     ```
   - No **Linux/macOS**:
     ```bash
     source envemotion/bin/activate
     ```

5. Instale as dependências necessárias:

```bash
pip install -r requirements
```

6. Coloque os modelos de rosto e emoções na pasta `models/`.

## Uso

Para rodar o projeto, basta executar o arquivo `main.py`:

```bash
python main.py
```

Isso abrirá a webcam, começará a capturar o vídeo e irá processar cada quadro para detectar e classificar emoções. Pressione a tecla **"Q"** para sair da aplicação.

### Parâmetros de Configuração

Você pode ajustar as configurações no arquivo `config.py`, onde é possível definir o caminho para os modelos e as labels de emoções.

## Contribuição

Sinta-se à vontade para fazer fork deste repositório e enviar pull requests com melhorias ou correções de bugs.

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature-nome`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature-nome`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
## 