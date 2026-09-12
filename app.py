import os
import html
import urllib.parse
import time
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
        "<h3 style='color: #ffffff; font-weight: 800; margin-bottom: 15px;'>"
        "📋 Revise os detalhes do seu pedido:"
        "</h3>",
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
        unsafe_allow_html=True
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
        border-radius: 12px !important;
        padding: 12px 24px !important;
        background-color: #1e293b !important;
        color: #94a3b8 !important;
        border: 1px solid #334155 !important;
        margin-right: 8px !important;
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
        background-color: #22c55e !important;
        border: none !important;
        border-radius: 12px !important;
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
    "logo.png", "logo.jpg", "logo.jpeg", "logo.webp",
    "Logo.png", "Logo.jpg", "LOGO.PNG", "LOGO.JPG"
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
    st.markdown('</div>', unsafe_allow_html=True)

st.title("🍢 Cuca Espetinhos e Lanches")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 16px; margin-bottom: 25px;'>Monte seu pedido de forma rápida e prática</p>", unsafe_allow_html=True)

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
            "preco": 9.00,
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
        "HOT FRANGO (Salsinha, frango, purê, batata palha, catchup, mostarda, maionese) ": {
            "preco": 14.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
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
        "PORÇÃO COMBO DE PORÇÕES": {
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
                st.markdown(f"<span class='preco-badge'>R$ {info['preco']:.2f}</span>", unsafe_allow_html=True)
                
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
                        "subtotal": info["preco"] * qtd
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
                        "➕ Adicionar Mais",
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
        st.button("✏️ Alterar Itens", on_click=voltar_ao_cardapio, use_container_width=True)

    st.markdown(f"### Subtotal: **R$ {subtotal_produtos:.2f}**")

    # Sanitização e limitação de caracteres do nome
    nome_bruto = st.text_input("Seu Nome:", max_chars=50, key="input_nome")
    nome = html.escape(nome_bruto.strip())

    tipo_entrega = st.radio(
        "Opção de Entrega:",
        ["Entrega", "Retirar no Local"],
        horizontal=True,
        key="input_tipo_entrega"
    )

    endereco = ""
    taxa_entrega = 0.00
    total_final = subtotal_produtos
    rua_numero = ""

    if tipo_entrega == "Entrega":
        bairro_selecionado = st.selectbox(
            "Selecione o Bairro:", list(taxas_bairros.keys()), key="input_bairro"
        )
        bairro = html.escape(bairro_selecionado)
        taxa_entrega = taxas_bairros.get(bairro_selecionado, 0.00)

        # Sanitização e limitação de caracteres do endereço
        rua_bruta = st.text_input("Rua e Número:", max_chars=100, key="input_rua")
        rua_numero = html.escape(rua_bruta.strip())

        if rua_numero:
            endereco = f"{rua_numero} - {bairro}"

        total_final += taxa_entrega
        if taxa_entrega > 0:
            st.info(f"🛵 Taxa de entrega para **{bairro}**: R$ {taxa_entrega:.2f}")
        else:
            st.warning("⚠️ Taxa de entrega a combinar via WhatsApp.")
    else:
        st.info("🏪 **Retirada no Balcão:** Sem taxa adicional.")

    st.markdown(f"## **Total Final: R$ {total_final:.2f}**")

    pagamento_selecionado = st.selectbox(
        "Forma de Pagamento", ["Pix", "Cartão", "Dinheiro"], key="input_pagamento"
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

    texto_pagamento = f"Pix (Chave: {CHAVE_PIX_VAL})" if pagamento == "Pix" else pagamento

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
        key="btn_avancar_confirmacao"
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
