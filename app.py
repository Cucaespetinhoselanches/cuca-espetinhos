import html
import os
import time
import urllib.parse
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

# ==================== GERENCIAMENTO SEGURO DE SEGREDOS ====================
WHATSAPP_NUMBER = st.secrets.get("WHATSAPP_NUMBER", "5512992093751")
CHAVE_PIX_VAL = st.secrets.get("CHAVE_PIX", "19919105848")

# ==================== ESTADOS DA SESSÃO ====================
if "mostrar_modal" not in st.session_state:
    st.session_state["mostrar_modal"] = False

if "etapa_pedido" not in st.session_state:
    st.session_state["etapa_pedido"] = "cardapio"

if "ultimo_item_alterado" not in st.session_state:
    st.session_state["ultimo_item_alterado"] = None

if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = {}

if "ultimo_envio_timestamp" not in st.session_state:
    st.session_state["ultimo_envio_timestamp"] = 0


# Funções Callback e Navegação
def registrar_alteracao_item(chave_item):
    if st.session_state.get(chave_item, 0) > 0:
        st.session_state["ultimo_item_alterado"] = chave_item
    else:
        if chave_item in st.session_state["carrinho"]:
            del st.session_state["carrinho"][chave_item]
        if st.session_state.get("ultimo_item_alterado") == chave_item:
            st.session_state["ultimo_item_alterado"] = None


def avancar_para_entrega():
    st.session_state["etapa_pedido"] = "dados_entrega"


def continuar_comprando():
    st.session_state["ultimo_item_alterado"] = None
    st.session_state["etapa_pedido"] = "cardapio"


def voltar_ao_cardapio():
    st.session_state["etapa_pedido"] = "cardapio"


# ==================== MODAL DE CONFIRMAÇÃO ====================
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, mensagem_texto):
    st.markdown(
        """
    <style>
        /* Estilização verde do botão de envio no WhatsApp */
        div.stLinkButton > a[kind="primary"],
        div.stLinkButton > a {
            background-color: #25D366 !important;
            color: #ffffff !important;
            border: none !important;
            font-weight: bold !important;
        }

        div.stLinkButton > a:hover {
            background-color: #1eb857 !important;
            color: #ffffff !important;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Sanitização contra Cross-Site Scripting (XSS)
    mensagem_html = html.escape(mensagem_texto).replace("\n", "<br>")
    st.markdown(
        f"""
        <div style='background-color: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #334155; font-size: 18px; line-height: 1.6; color: #f8fafc;'>
            {mensagem_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    link_whatsapp = (
        f"https://wa.me/{numero_wa}?text={urllib.parse.quote(mensagem_texto)}"
    )

    st.write("---")
    col_voltar, col_enviar = st.columns([1, 2])

    with col_voltar:
        if st.button("❌ Alterar Pedido", use_container_width=True):
            st.session_state["mostrar_modal"] = False
            st.rerun()

    with col_enviar:
        st.link_button(
            "📲 CONFIRMAR E ENVIAR",
            link_whatsapp,
            type="primary",
            use_container_width=True,
        )


# --- ESTILIZAÇÃO CSS CUSTOMIZADA ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a !important;
        color: #f8fafc !important;
    }

    h1 {
        font-size: 32px !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 5px !important;
    }

    .logo-container img {
        max-height: 150px !important;
        width: auto !important;
        margin: 0 auto;
        display: block;
        object-fit: contain !important;
    }

    div[data-testid="stColumn"] img {
        max-height: 120px !important;
        object-fit: cover !important;
        border-radius: 10px !important;
    }

    div[data-testid="stColumn"] > div {
        background-color: #1e293b !important;
        border-radius: 16px;
        padding: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        border: 1px solid #334155 !important;
        margin-bottom: 10px;
    }

    label, p, span, div {
        color: #f8fafc !important;
    }

    button[data-baseweb="tab"] {
        font-size: 20px !important;
        font-weight: 800 !important;
        padding: 12px 24px !important;
        background-color: #1e293b !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #ef4444 !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
    }

    .preco-badge {
        background-color: #15803d !important;
        color: #ffffff !important;
        font-weight: 900;
        font-size: 20px !important;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
        margin-top: 4px;
        margin-bottom: 4px;
    }

    div[data-testid="stNumberInput"] input {
        font-size: 20px !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        text-align: center !important;
        height: 42px !important;
    }

    div[data-testid="stNumberInput"] button {
        height: 42px !important;
        width: 42px !important;
        background-color: #334155 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }

    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        background-color: #334155 !important;
        color: #ffffff !important;
        border: 1px solid #475569 !important;
    }

    div.stButton > button[kind="primary"], div.stLinkButton > a[kind="primary"] {
        background-color: #D96B27 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
    }

    div.stButton > button[kind="primary"] p, div.stLinkButton > a[kind="primary"] p {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 18px !important;
    }

    div[data-testid="stNotification"] {
        background-color: #064e3b !important;
        border-left: 5px solid #22c55e !important;
        border-radius: 12px !important;
    }
    div[data-testid="stNotification"] p {
        color: #ecfdf5 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==================== CARREGAMENTO SEGURO DA LOGO ====================
opcoes_logo = [
    "logo.png",
    "logo.jpg",
    "logo.jpeg",
    "logo.webp",
    "Logo.png",
    "Logo.jpg",
    "LOGO.PNG",
    "LOGO.JPG",
]

logo_encontrada = None
for nome_arquivo in opcoes_logo:
    # Validação rigorosa de caminho (prevenção contra Directory Traversal)
    caminho_abs = os.path.abspath(nome_arquivo)
    if caminho_abs.startswith(os.getcwd()) and os.path.exists(nome_arquivo):
        logo_encontrada = nome_arquivo
        break

if logo_encontrada:
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    st.image(logo_encontrada, use_container_width=False, width=180)
    st.markdown("</div>", unsafe_allow_html=True)

st.title("🍢 Cuca Espetinhos e Lanches")
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 16px; margin-bottom: 25px;'>Monte seu pedido de forma rápida e prática</p>",
    unsafe_allow_html=True,
)

menu_categorias = {
    "🍢 Espetos": {
        "ESPETO PÃO DE ALHO": {
            "preco": 9.00,
            "imagem": "https://casadecarnesdomaninho.com.br/wp-content/uploads/2022/06/espetinho-pao-de-alho.jpg",
        },
        "ESPETO ROMEU E JULIETA (Bacon/Goiabada/Queijo)": {
            "preco": 15.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO QUEIJO COALHO": {
            "preco": 9.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpyXQSm25u3do9kGas7sKk1Lf1oXX7mcrS5IC9w5UPKUfGRAdrjq2a8vFs&s=10",
        },
        "ESPETO PANCETA": {
            "preco": 12.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO ALCATRA": {
            "preco": 12.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO PICANHA": {
            "preco": 18.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO FRALDINHA": {
            "preco": 12.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO LINGUIÇA": {
            "preco": 9.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO LINGUIÇA GOURMET": {
            "preco": 14.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO KAFTA": {
            "preco": 12.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO KAFTA GOURMET": {
            "preco": 14.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO CORAÇÃO": {
            "preco": 18.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "ESPETO FRANGO": {
            "preco": 12.00,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
    },
    "🥪 Lanches": {
        "X-BURGER (Hamburguer, queijo cheedar Polenghi e molho da casa)": {
            "preco": 19.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "X-SALADA (Hamburguer, queijo cheedar Polenghi, alface americana, tomate e molho da casa)": {
            "preco": 29.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "X-BACON (Hamburguer, bacon, queijo cheedar Polenghi, alface americana, tomate e molho da casa)": {
            "preco": 35.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "X-EGG (Hamburguer, ovo, queijo cheedar Polenghi, alface americana, tomate e molho da casa)": {
            "preco": 30.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "X-CATUPIRY EMPANADO (Empanado de Catupiry com frango, queijo cheedar Polenghi, alface americana, tomate e molho da casa)": {
            "preco": 32.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "X-CATUPIRY EMPANADO 2.0 (Empanado de Catupiry com frango, hamburguer, queijo cheedar Polenghi, alface americana, tomate e molho da casa)": {
            "preco": 41.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "FRANGÃO (Hamburguer, frango desfiado, queijo cheedar Polenghi, alface americana, tomate e molho da casa)": {
            "preco": 32.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "HOT SIMPLES (Salsinha, batata palha, catchup, mostarda, maionese)": {
            "preco": 16.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
        },
        "HOT PURÊ (Salsinha, purê, batata palha, catchup, mostarda, maionese)": {
            "preco": 16.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
        },
        "HOT CALABRESA (Salsinha, calabresa, purê, batata palha, catchup, mostarda, maionese)": {
            "preco": 16.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
        },
        "HOT BACON (Salsinha, bacon, purê, batata palha, catchup, mostarda, maionese)": {
            "preco": 16.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
        },
        "HOT SALADA (Salsinha, salada, purê, batata palha, catchup, mostarda, maionese)": {
            "preco": 12.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
        },
        "HOT FRANGO (Salsinha, frango, purê, batata palha, catchup, mostarda, maionese)": {
            "preco": 14.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
        },
        "Monte seu combo (Acrescente: Batata frita + refrigerante em lata ao seu lanche POR:)": {
            "preco": 14.90,
            "imagem": "https://imagens.jotaja.com/produtos/496ecdc0-4019-489f-8744-01c8417784c0.jpg",
        },
        "Turbine seu lanche (Acrescente 1 hamburguer POR:)": {
            "preco": 7.00,
            "imagem": "https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f680.gif",
        },
        "Turbine seu lanche (Acrescente BACON POR:)": {
            "preco": 5.00,
            "imagem": "https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f680.gif",
        },
        "Turbine seu lanche (Acrescente CHEDDAR POR:)": {
            "preco": 5.00,
            "imagem": "https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f680.gif",
        },
        "Turbine seu lanche (Acrescente SALSICHA POR:)": {
            "preco": 5.00,
            "imagem": "https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f680.gif",
        },
        "Turbine seu lanche (Acrescente CATUPIRY POR:)": {
            "preco": 12.00,
            "imagem": "https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f680.gif",
        },
        "Turbine seu lanche (Acrescente FRANGO DESFIADO POR:)": {
            "preco": 7.00,
            "imagem": "https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f680.gif",
        },
        "Turbine seu lanche (Acrescente PURE POR:)": {
            "preco": 5.00,
            "imagem": "https://images.emojiterra.com/google/noto-emoji/animated-emoji/1f680.gif",
        },
        
    },
    
    "🍟 Porções": {
        "PORÇÃO BATATA FRITA": {
            "preco": 29.90,
            "imagem": "https://2.bp.blogspot.com/-zNkU0qa51Uk/U5elL6RgI6I/AAAAAAAAACo/OngayLy9ogk/s1600/batata.jpg",
        },
        "PORÇÃO MANDIOCA FRITA": {
            "preco": 29.90,
            "imagem": "https://media.istockphoto.com/id/903103922/pt/foto/brazilian-food-mandioca-frita-deep-fried-cassava-root.webp?a=1&b=1&s=612x612&w=0&k=20&c=KwVZFUrGJlRkXM6_nyBNPt_6sbpHJ1x0pR49fA2wIgY=",
        },
        "PORÇÃO ANÉIS DE CEBOLA": {
            "preco": 28.90,
            "imagem": "https://images.unsplash.com/photo-1766589152292-3c052f0d87aa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHBvciVDMyVBNyVDMyVBM28lMjBhbmVpcyUyMGRlJTIwY2Vib2xhfGVufDB8fDB8fHww",
        },
        "PORÇÃO DE MOELA (SOMENTE AOS SABADOS)": {
            "preco": 34.90,
            "imagem": "data:image/webp;base64,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",
        },
        "PORÇÃO - COMBO DE PORÇÕES (Batata e mandioca frita, aneis de cebola)": {
            "preco": 49.90,
            "imagem": "https://images.unsplash.com/photo-1702827495434-629df15aa136?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fHBvciVDMyVBNyVDMyVBM28lMjBjb21ib3xlbnwwfHwwfHx8MA%3D%3D",
        },
    },
    "🥤 Refrigerantes": {
        "Refrigerante COCA NORMAL Lata 350ml": {
            "preco": 6.00,
            "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
        },
        "Refrigerante COCA ZERO Lata 350ml": {
            "preco": 6.00,
            "imagem": "https://acdn-us.mitiendanube.com/stores/001/165/503/products/coca-zero21-16e7cba0588363da7616192142363168-1024-1024.webp",
        },
        "Refrigerante FANTA LARANJA Lata 350ml": {
            "preco": 6.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCj-iJ_ziGZMurwiupsfzkhhmuRr4vDxjEM4V3QapNpg&s=10",
        },
        "Refrigerante SPRITE Lata 350ml": {
            "preco": 6.00,
            "imagem": "https://www.drogariaminasbrasil.com.br/media/webp/catalog/product/cache/74c1057f7991b4edb2bc7bdaa94de933/image/228324e3d/refrigerante-sprite-lata-350ml_jpg.webp",
        },
        "Refrigerante FANTA UVA Lata 350ml": {
            "preco": 6.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy8MfxKAF9fZHoP5jOkB_GVC3llWVFJgX8bqaQQsBNTw&s=10",
        },
        "Refrigerante GUARANA ANTARCTICA Lata 350ml": {
            "preco": 6.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRo_of1b4lkVoGXo7VNDcQ2zcyItH2BvZ-A2XFU362rbA&s=10",
        },
        "Refrigerante TONICA SCHWEPPES Lata 350ml": {
            "preco": 6.50,
            "imagem": "https://www.imigrantesbebidas.com.br/bebida/images/products/full/2209-agua-tonica-schweppes-lata-350ml.jpg",
        },
        "Refrigerante FANTA LARANJA Garrafinha 200ml": {
            "preco": 3.50,
            "imagem": "https://mercantilatacado.vtexassets.com/arquivos/ids/172941/654a33c475d9096810e2cbfc.jpg?v=638349585366670000",
        },
        "Refrigerante COCA COLA Garrafinha 200ml": {
            "preco": 3.50,
            "imagem": "https://mercantilnovaera.vtexassets.com/arquivos/ids/181329/Refrigerante-COCA-COLA-Garrafa-Pet-200ml.jpg?v=637602425279600000",
        },
        "Refrigerante COCA ZERO Garrafinha 200ml": {
            "preco": 3.50,
            "imagem": "https://prezunic.vtexassets.com/arquivos/ids/210276-800-auto?v=638568370331100000&width=800&height=auto&aspect=true",
        },
        "Refrigerante GUARANITA Garrafinha 200ml": {
            "preco": 3.50,
            "imagem": "https://phygital-files.mercafacil.com/fernandes-bucket/uploads/produto/cibal_guaranita_200ml_4762cf0e-e46e-4cb8-b0cf-5e3c11785572.jpg",
        },
        "Refrigerante SPRITE Garrafinha 200ml": {
            "preco": 3.50,
            "imagem": "https://mercantilnovaera.vtexassets.com/arquivos/ids/170425/Refrigerante-Limao-Sprite-Garrafa-200ml.jpg?v=637442546240970000",
        },
        "Refrigerante COCA COLA 2L": {
            "preco": 17.00,
            "imagem": "https://gbarbosa.vtexassets.com/arquivos/ids/214289/655268ba8d0743e14888f712.jpg?v=638354963814100000",
        },
        "Refrigerante PEPSI 2L": {
            "preco": 17.00,
            "imagem": "https://hiperideal.vtexassets.com/arquivos/ids/228374/7892840800000-RefrigerantePEPSIGarrafa2L-1.jpg?v=638733302785230000",
        },
        "Refrigerante COCA ZERO 2.5L": {
            "preco": 17.00,
            "imagem": "https://mercantilnovaera.vtexassets.com/arquivos/ids/230310/45911-1779911965249.png.png?v=639155088729770000",
        },
        "Refrigerante COCA ZERO 1L": {
            "preco": 10.00,
            "imagem": "https://mercantilatacado.vtexassets.com/arquivos/ids/168646/653fe3aa752720c144887a35.jpg?v=638342826762370000",
        },
        "Refrigerante H20 500ml": {
            "preco": 8.00,
            "imagem": "https://savegnagoio.vtexassets.com/arquivos/ids/447261-800-800?v=638525058304970000&width=800&height=800&aspect=true",
        },
        "Refrigerante TONICA SCHWEPPES 600ml": {
            "preco": 8.00,
            "imagem": "https://almacenestampico.com/wp-content/uploads/2023/03/Almacenes-Tampico-Uruguay-agua-tonica-schwepps-600Mesa-de-trabajo-1.jpg",
        },
        "Refrigerante FANTA UVA 600ml": {
            "preco": 8.00,
            "imagem": "https://io.convertiez.com.br/m/farmaciasaopaulo/shop/products/images/16728/medium/fanta-uva-600ml_25847.jpg",
        },
        "Refrigerante SPRITE 600ml": {
            "preco": 8.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxBTxJckfXC_FK2APRFPRLnVY8tC68jlixc3fnLgPZAg&s",
        },
        "Refrigerante GUARANITA 600ml": {
            "preco": 8.00,
            "imagem": "https://tauste.com.br/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/1/5/1584431777359902.jpg",
        },
        "Refrigerante COCA COLA 600ml": {
            "preco": 8.00,
            "imagem": "https://bretas.vtexassets.com/arquivos/ids/182991-800-auto?v=638375498920300000&width=800&height=auto&aspect=true",
        },
        "Refrigerante COCA COLA ZERO 600ml": {
            "preco": 8.00,
            "imagem": "https://mercantilnovaera.vtexassets.com/arquivos/ids/232442/Refrigerante-COCA-COLA-Zero-Acucar-Pet-600ml.jpg?v=639179091417330000",
        },
        "Refrigerante FANTA 600ml": {
            "preco": 8.00,
            "imagem": "https://phygital-files.mercafacil.com/miliozzi/uploads/produto/refrigerante_fanta_laranja_600ml_pet_a8b5c222-e21b-480c-8288-90e22dbb20d7.jpg",
        },
        "AGUA MINERAL SEM GAS 500ml": {
            "preco": 3.00,
            "imagem": "https://io.convertiez.com.br/m/farmaponte/shop/products/images/22004/medium/agua-mineral-crystal-sem-gas-garrafa-1-unidade-com-500ml_17652.webp",
        },
        "AGUA MINERAL COM GAS 500ml": {
            "preco": 4.00,
            "imagem": "https://apoioentrega.vteximg.com.br/arquivos/ids/1911515/139272_0.png?v=639213665179000000",
        },
    },
    "🍺 Cervejas": {
        "Cerveja Original 300ml Garrafinha": {
            "preco": 6.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRllDI7RJyBsZMII0SR2UZhiYstauUqjyhKbGznH27HEw&s=10",
        },
        "Cerveja Budweiser 300ml Garrafinha": {
            "preco": 6.00,
            "imagem": "https://phygital-files.mercafacil.com/comercial-catanio-supermercado/uploads/produto/cerveja_budweiser_garrafinha_300ml_61022027-0c5d-4d8b-9f9f-620188027143.jpg",
        },
        "Cerveja Antarctica 300ml Garrafinha": {
            "preco": 5.00,
            "imagem": "https://nunesbebidas.com.br/wp-content/uploads/2021/05/Nunes-Bebidas-CERVEJA-ANTARTICA-BOA-GARRAFA-300ML.jpg",
        },
        "Cerveja Brahma 300ml Garrafinha": {
            "preco": 5.00,
            "imagem": "https://assets.ibecom.com.br/ib.item.image.large/l-27778dbad9724b6fb9695e6315f029e1.jpeg",
        },
        "Cerveja Império 300ml Garrafinha": {
            "preco": 5.00,
            "imagem": "https://assets.ibecom.com.br/ib.item.image.large/l-ab81028dfcae4433a707b191cbe67d8c.jpeg",
        },
        "Cerveja Skol 269ml Lata": {
            "preco": 5.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSWuMoEZy8_ZGbuqI12QrAUkAjTrwh2VPt6KqEXh8CR6pzKGxtSKXBlQfz&s=10",
        },
        "Cerveja Budweiser 269ml Lata": {
            "preco": 6.00,
            "imagem": "https://mambodelivery.vtexassets.com/arquivos/ids/212124-800-450?v=638537266038970000&width=800&height=450&aspect=true",
        },
        "Cerveja Original 269ml Lata": {
            "preco": 6.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsK7x1diT-koyfCAdWSUBoHZTgPloiJYMjbRSfxGJzaw&s=10",
        },
        "Cerveja Amstel 269ml Lata": {
            "preco": 5.00,
            "imagem": "https://m.media-amazon.com/images/I/61gLfj5ExrL._AC_UF1000,1000_QL80_.jpg",
        },
        "Cerveja Império 269ml Lata": {
            "preco": 5.00,
            "imagem": "https://bretas.vtexassets.com/arquivos/ids/202744-800-auto?v=638376354703200000&width=800&height=auto&aspect=true",
        },
        "Cerveja Brahma Duplo Malte 269ml Lata": {
            "preco": 6.00,
            "imagem": "https://a-static.mlcdn.com.br/420x420/cerveja-brahma-duplo-malte-lager-15-unidades-lata-269ml/jrr/0f7b0dc65aa911ecb4ca4201ac18503a/3faba7ce5a536589f67a76512b5cbf98.jpg",
        },
        "Cerveja Long Neck Heineken": {
            "preco": 10.00,
            "imagem": "https://images.unsplash.com/photo-1618885472179-5e474019f2a9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Z2FycmFmYSUyMGRlJTIwY2VydmVqYXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "Cerveja Long Neck Budweiser": {
            "preco": 10.00,
            "imagem": "https://images.unsplash.com/photo-1587669284207-e8ee0fc74144?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Z2FycmFmYSUyMGRlJTIwY2VydmVqYXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "Cerveja Long Neck Corona": {
            "preco": 10.00,
            "imagem": "https://images.unsplash.com/photo-1600213903598-25be92abde40?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Z2FycmFmYSUyMGRlJTIwY2VydmVqYXxlbnwwfHwwfHx8MA%3D%3D",
        },
        "Energético Monster 473ml": {
            "preco": 14.00,
            "imagem": "https://andinacocacola.vtexassets.com/arquivos/ids/158541/112666_COCA---MONSTER_GREEN__LT_473ML.jpg?v=639238910718900000",
        },
        "Cerveja Amstel 350ml Lata": {
            "preco": 6.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqQ_3JZ9bzr9LODFFj1Lps0OroT6jJ_PrC24CiZ0nEHg&s=10",
        },
        "Cerveja Império 350ml Lata": {
            "preco": 6.00,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXKTXeRvTYQBjWEX-eei2xutbAx97LRhZnpOrEEQ_5Dg&s=10",
        },
        "Cerveja Brahma Duplo Malte 350ml Lata": {
            "preco": 7.00,
            "imagem": "https://hortifrutibr.vtexassets.com/arquivos/ids/173202/Cerveja-Brahma-Duplo-Malte-Lata-Sleek-350Ml.png?v=639239767332900000",
        },
    },
}

taxas_bairros = {
    "Nova Jacareí": 3.00,
    "Igarapés": 5.00,
    "Esperança": 4.00,
    "Centro": 8.00,
    "São Luiz": 5.00,
    "Portal": 5.00,
    "Jd. São Paulo": 5.00,
    "Terras de São João": 5.00,
    "Jd. Emilia": 7.00,
    "1 de maio": 5.00,
    "Jd. Alvorada": 5.00,
    "Imperial": 5.00,
    "Pedramar": 7.00,
    "Ijal": 5.00,
    "São João": 6.00,
    "Panorama": 7.00,
    "Jd. Didinha": 7.00,
}

# ==================== EXIBIÇÃO DO CARDÁPIO ====================
abas = st.tabs(list(menu_categorias.keys()))

for aba, (categoria, itens) in zip(abas, menu_categorias.items()):
    with aba:
        for item, info in itens.items():
            chave_item = f"{categoria}_{item}"
            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(info["imagem"], use_container_width=True)
            with col2:
                st.markdown(f"**{item}**")
                st.markdown(
                    f"<span class='preco-badge'>R$ {info['preco']:.2f}</span>",
                    unsafe_allow_html=True,
                )

                # Validação de limite máximo de unidades por item
                qtd = st.number_input(
                    "Qtd:",
                    min_value=0,
                    max_value=20,
                    step=1,
                    key=chave_item,
                    label_visibility="collapsed",
                    on_change=registrar_alteracao_item,
                    args=(chave_item,),
                )

                if qtd > 0:
                    st.session_state["carrinho"][chave_item] = {
                        "item": item,
                        "qtd": qtd,
                        "subtotal": info["preco"] * qtd,
                    }

            if (
                st.session_state.get("ultimo_item_alterado") == chave_item
                and qtd > 0
                and st.session_state["etapa_pedido"] == "cardapio"
            ):
                st.info(f"✅ **{qtd}x {item}** adicionado!")
                st.markdown("**O que deseja fazer agora?**")

                col_mais, col_encerrar = st.columns(2)
                with col_mais:
                    st.button(
                        "➕ Adicionar ITENS",
                        key=f"btn_mais_{chave_item}",
                        use_container_width=True,
                        on_click=continuar_comprando,
                    )

                with col_encerrar:
                    st.button(
                        "✅ Finalizar Pedido",
                        key=f"btn_encerrar_{chave_item}",
                        type="primary",
                        use_container_width=True,
                        on_click=avancar_para_entrega,
                    )

itens_carrinho = list(st.session_state["carrinho"].values())
subtotal_produtos = sum(i["subtotal"] for i in itens_carrinho)

# ==================== DADOS DE ENTREGA E PAGAMENTO ====================
if itens_carrinho and st.session_state["etapa_pedido"] == "dados_entrega":
    st.markdown("<div id='secao-entrega'></div>", unsafe_allow_html=True)

    st.write("---")
    col_titulo, col_voltar_btn = st.columns([3, 1])
    with col_titulo:
        st.subheader("📦 Entrega & Pagamento")
    with col_voltar_btn:
        st.button(
            "✏️ Alterar Itens",
            on_click=voltar_ao_cardapio,
            use_container_width=True,
        )

    # Resumo rápido dos itens selecionados
    with st.expander("🛒 Ver itens do carrinho", expanded=False):
        for item_cart in itens_carrinho:
            st.write(
                f"• {item_cart['qtd']}x **{item_cart['item']}** — R$ {item_cart['subtotal']:.2f}"
            )

    st.markdown(f"### Subtotal: **R$ {subtotal_produtos:.2f}**")

    # Sanitização e limitação de caracteres do nome
    nome_bruto = st.text_input("Seu Nome:", max_chars=50, key="input_nome")
    nome = html.escape(nome_bruto.strip())

    tipo_entrega = st.radio(
        "Opção de Entrega:",
        ["Entrega", "Retirar no Local"],
        horizontal=True,
        key="input_tipo_entrega",
    )

    endereco = ""
    taxa_entrega = 0.00
    total_final = subtotal_produtos
    rua_numero = ""

    if tipo_entrega == "Entrega":
        bairro_selecionado = st.selectbox(
            "Selecione o Bairro:",
            list(taxas_bairros.keys()),
            key="input_bairro",
        )
        bairro = html.escape(bairro_selecionado)
        taxa_entrega = taxas_bairros.get(bairro_selecionado, 0.00)

        # Sanitização e limitação de caracteres do endereço
        rua_bruta = st.text_input(
            "Rua e Número:", max_chars=100, key="input_rua"
        )
        rua_numero = html.escape(rua_bruta.strip())

        if rua_numero:
            endereco = f"{rua_numero} - {bairro}"

        total_final += taxa_entrega
        if taxa_entrega > 0:
            st.info(
                f"🛵 Taxa de entrega para **{bairro}**: R$ {taxa_entrega:.2f}"
            )
        else:
            st.warning("⚠️ Taxa de entrega a combinar via WhatsApp.")
    else:
        st.info("🏪 **Retirada no Balcão:** Sem taxa adicional.")

    st.markdown(f"## **Total Final: R$ {total_final:.2f}**")

    pagamento_selecionado = st.selectbox(
        "Forma de Pagamento",
        ["Pix", "Cartão", "Dinheiro"],
        key="input_pagamento",
    )
    pagamento = html.escape(pagamento_selecionado)

    if pagamento == "Pix":
        st.markdown(
            f"""
            <div style='background-color: #064e3b; border-left: 5px solid #22c55e; padding: 15px; border-radius: 12px; margin-bottom: 15px;'>
                <p style='color: #ecfdf5 !important; font-size: 18px !important; margin-bottom: 5px;'>📱 <b>Chave PIX (Telefone):</b></p>
                <p style='color: #22c55e !important; font-size: 26px !important; font-weight: 900 !important; letter-spacing: 1px; margin: 0;'>{CHAVE_PIX_VAL}</p>
                <p style='color: #94a3b8 !important; font-size: 14px !important; margin-top: 8px;'><i>Por favor, envie o comprovante pelo WhatsApp após finalizar o pedido.</i></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    itens_txt = "\n".join(
        [
            f"{i['qtd']}x {html.escape(i['item'])} (R$ {i['subtotal']:.2f})"
            for i in itens_carrinho
        ]
    )

    if tipo_entrega == "Entrega":
        detalhes_tipo = f"*Tipo:* Entrega\n*Endereço:* {endereco}\n*Taxa:* R$ {taxa_entrega:.2f}"
    else:
        detalhes_tipo = "*Tipo:* Retirada no Local"

    texto_pagamento = (
        f"Pix (Chave: {CHAVE_PIX_VAL})" if pagamento == "Pix" else pagamento
    )

    mensagem = (
        f"Olá! Gostaria de fazer um pedido na *Cuca Espetinhos e Lanches*:\n\n"
        f"*Cliente:* {nome}\n"
        f"{detalhes_tipo}\n"
        f"*Pagamento:* {texto_pagamento}\n\n"
        f"*Itens:*\n{itens_txt}\n\n"
        f"*Total a Pagar:* R$ {total_final:.2f}"
    )

    if st.button(
        "🚀 AVANÇAR PARA CONFIRMAÇÃO",
        type="primary",
        use_container_width=True,
        key="btn_avancar_confirmacao",
    ):
        agora = time.time()
        # Trava simples de rate limit por sessão (mínimo 3s entre cliques)
        if agora - st.session_state["ultimo_envio_timestamp"] < 3:
            st.warning("Aguarde um instante antes de clicar novamente.")
        elif tipo_entrega == "Entrega" and not rua_numero:
            st.error("Por favor, preencha a Rua e o Número para continuar.")
        elif not nome:
            st.error("Por favor, informe seu nome para continuar.")
        else:
            st.session_state["ultimo_envio_timestamp"] = agora
            st.session_state["mostrar_modal"] = True

    if st.session_state.get("mostrar_modal", False):
        modal_confirmacao(WHATSAPP_NUMBER, mensagem)

    components.html(
        """
        <script>
            var elemento = window.parent.document.getElementById('secao-entrega');
            if (elemento) {
                elemento.scrollIntoView({behavior: 'smooth'});
            }
        </script>
        """,
        height=0,
    )
