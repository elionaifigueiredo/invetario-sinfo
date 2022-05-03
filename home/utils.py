from turtle import left, position, right
from django.db import router
import matplotlib.pyplot as plt

import base64

from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,3))
    plt.subplot(131)
    plt.title('Material Carga')
    plt.bar(x,y, color='tab:orange')
   
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.xlabel('Itens', fontsize=10, color='red')
    plt.ylabel('Série')
    plt.tight_layout()
    graph = get_graph()
    return graph