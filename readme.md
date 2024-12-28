# People Tracking with YOLOv7

Este projeto é uma implementação de rastreamento de pessoas usando o modelo YOLOv7. Ele permite a detecção e rastreamento de pessoas em vídeos ou transmissões ao vivo, e inclui uma interface gráfica para facilitar o uso.

## Funcionalidades

- Detecção de pessoas usando YOLOv7.
- Rastreamento de pessoas usando o algoritmo SORT.
- Cálculo da distância percorrida por cada pessoa.
- Interface gráfica para configuração e execução do processo de detecção e rastreamento.

## Requisitos

- Python 3.7+
- Bibliotecas Python:
    - `numpy`
    - `opencv-python`
    - `torch`
    - `tkinter`
    - `filterpy`
    - `scipy`
    - `tqdm`

## Instalação

1. Clone o repositório:

     ```sh
     git clone https://github.com/seu-usuario/people-tracking-yolov7.git
     cd people-tracking-yolov7
     ```

2. Crie um ambiente virtual e ative-o:

     ```sh
     python -m venv venv
     source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
     ```

3. Instale as dependências:

     ```sh
     pip install -r requirements.txt
     ```

4. Baixe os pesos do modelo YOLOv7x:

     ```sh
     python utils/download_weights.py
     ```

## Uso

### Interface Gráfica

1. Execute o script `interface.py`:

     ```sh
     python interface.py
     ```

2. Use a interface gráfica para:
     - Selecionar o arquivo de vídeo ou a câmera.
     - Selecionar o arquivo de pesos do modelo.
     - Configurar os parâmetros desejados.
     - Iniciar o processo de detecção e rastreamento.

### Linha de Comando

Você também pode executar o script de detecção e rastreamento diretamente pela linha de comando:

```sh
python detect_and_track.py --source <source> --weights <weights> --img-size <img_size> --conf-thres <conf_thres> --iou-thres <iou_thres> --device <device> --view-img --save-txt --save-img --classes <classes> --agnostic-nms --augment
```

## Estrutura do Projeto

```plaintext
people-tracking-yolov7/
├── detect_and_track.py
├── interface.py
├── models/
│   └── experimental.py
├── sort.py
├── utils/
│   ├── datasets.py
│   ├── download_weights.py
│   ├── general.py
│   ├── plots.py
│   └── torch_utils.py
├── requirements.txt
└── README.md
```

## Créditos

Este projeto foi baseado no repositório [people-tracking-yolov7](https://github.com/noorkhokhar99/people-tracking-yolov7) de [noorkhokhar99](https://github.com/noorkhokhar99).

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
