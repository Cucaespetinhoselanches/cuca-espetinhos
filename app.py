import urllib.parse
import streamlit as st

# Inicializa a memória da sessão para controle do modal
if "mostrar_modal" not in st.session_state:
    st.session_state["mostrar_modal"] = False

# ==================== FUNÇÃO DO MODAL DE CONFIRMAÇÃO ====================
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, mensagem_texto):
    st.write("### Revise os detalhes do seu pedido:")
    st.info(mensagem_texto)

    link_whatsapp = f"https://wa.me/{numero_wa}?text={urllib.parse.quote(mensagem_texto)}"

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
# =======================================================================

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

# --- ESTILIZAÇÃO CUSTOMIZADA DE FONTES E BOTÕES ---
st.markdown("""
    <style>
    /* Aumenta a fonte geral dos rótulos de campos e entradas */
    label, div[data-testid="stMarkdownContainer"] p {
        font-size: 18px !important;
    }

    /* Aumenta os títulos das seções */
    h1 { font-size: 32px !important; }
    h2 { font-size: 26px !important; }
    h3 { font-size: 22px !important; }

    /* Destaque para os preços nos itens */
    .preco-destaque {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #2e7d32 !important; /* Verde escuro para contraste */
    }

    /* Aumenta a fonte e o tamanho de TODOS os botões do Streamlit */
    div.stButton > button {
        font-size: 20px !important;
        font-weight: bold !important;
        min-height: 3.2em !important;
        border-radius: 10px !important;
    }

    /* Estilização específica do botão VERDE (Primary / WhatsApp) */
    div.stLinkButton > a[kind="primary"], div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 3.5em !important;
        font-size: 22px !important;
        font-weight: bold !important;
        background-color: #25D366 !important; /* Verde oficial WhatsApp */
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    div.stLinkButton > a[kind="primary"]:hover, div.stButton > button[kind="primary"]:hover {
        background-color: #1EBE5D !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Exibe o logo local salvo na pasta do projeto
st.image("logo.png", width=200)

st.title("🍢 Cuca Espetinhos e Lanches")

# Cardápio
menu = {
    "X BURGER": {
        "preco": 19.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X SALADA": {
        "preco": 29.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X BACON": {
        "preco": 35.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X-EGG": {
        "preco": 30.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X-CATUPIRY EMPANADO": {
        "preco": 32.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "FRANGÃO": {
        "preco": 32.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "HOT CALABRESA": {
        "preco": 16.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "HOT BACON": {
        "preco": 16.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "HOT SALADA": {
        "preco": 12.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "HOT PURE": {
        "preco": 14.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "PORÇÃO BATATA FRITA": {
        "preco": 29.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1672774750509-bc9ff226f3e8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cG9yJUMzJUE3JUMzJUE3byUyMGJhdGF0YSUyMGZyaXRhfGVufDB8fDB8fHww",
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
    "ESPETO PÃO DE ALHO": {
        "preco": 9.00,
        "imagem": "data:image/jpeg;base64,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",
    },
    "ESPETO ROMEU E JULIETA (Bacon/Goiabada/Queijo)": {
        "preco": 15.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO QUEIJO COALHO": {
        "preco": 9.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO PANCETA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO ALCATRA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO PICANHA": {
        "preco": 18.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO FRALDINHA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO LINGUIÇA": {
        "preco": 9.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO LINGUIÇA GOURMET": {
        "preco": 9.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO KAFTA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO KAFTA GOURMET": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO CORAÇÃO": {
        "preco": 18.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO FRANGO": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "Refrigerante Lata": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    },
    "Suco Del Valle 200ml": {
        "preco": 8.00,
        "imagem": "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=400",
    },
    "Suco 1L": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=400",
    },
    "Cerveja Original 300ml Garrafinha": {
        "preco": 6.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Budweiser 300ml Garrafinha": {
        "preco": 6.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Antarctica 300ml Garrafinha": {
        "preco": 5.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Brahma 300ml Garrafinha": {
        "preco": 5.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Império 300ml Garrafinha": {
        "preco": 5.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Skol 269ml Lata": {
        "preco": 5.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Budweiser 269ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Original 269ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Amstel 269ml Lata": {
        "preco": 5.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Império 269ml Lata": {
        "preco": 5.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Brahma Duplo Malte 269ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
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
        "imagem": "https://images.unsplash.com/photo-1622543925917-763c34d1a86e?w=400",
    },
    "Cerveja Amstel 350ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Império 350ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Brahma Duplo Malte 350ml Lata": {
        "preco": 7.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
}

# Tabela de Bairros e Taxas de Entrega
taxas_bairros = {
    "Nova Jacareí": 3.00,
    "Igarapés": 5.00,
    "Esperança": 4.00,
    "São Luiz": 5.00,
    "Portal": 5.00,
    "Jardim São Paulo": 5.00,
    "Terras de São João": 5.00,
    "1º de Maio": 5.00,
    "Jardim Alvorada": 5.00,
    "Imperial": 5.00,
    "Pedramar": 7.00,
    "Ijal": 5.00,
    "São João": 6.00,
    "Centro": 8.00,
    "Panorama": 7.00,
    "Jardim Dindinha": 7.00,
    "Jardim Emília": 7.00,
    "Outro Bairro (A combinar)": 0.00,
}

carrinho = []
subtotal_produtos = 0.0

st.subheader("Faça seu Pedido")

for item, info in menu.items():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(info["imagem"], width=100)
    with col2:
        label_item = f"**{item}** — <span class='preco-destaque'>R$ {info['preco']:.2f}</span>"
        st.markdown(label_item, unsafe_allow_html=True)
        qtd = st.number_input(
            "Quantidade:",
            min_value=0,
            step=1,
            key=item,
            label_visibility="collapsed"
        )
        if qtd > 0:
            subtotal_item = info["preco"] * qtd
            carrinho.append(
                {"item": item, "qtd": qtd, "subtotal": subtotal_item}
            )
            subtotal_produtos += subtotal_item

if carrinho:
    st.divider()
    st.write(f"## **Subtotal dos itens: R$ {subtotal_produtos:.2f}**")

    nome = st.text_input("Seu Nome:")
    tipo_entrega = st.radio(
        "Opção de Entrega:",
        ["Entrega", "Retirar no Local"],
        horizontal=True,
    )

    endereco = ""
    taxa_entrega = 0.00
    total_final = subtotal_produtos

    if tipo_entrega == "Entrega":
        bairro = st.selectbox("Selecione o seu Bairro:", list(taxas_bairros.keys()))
        taxa_entrega = taxas_bairros[bairro]
        rua_numero = st.text_input("Rua e Número:")

        if rua_numero:
            endereco = f"{rua_numero} - {bairro}"

        total_final += taxa_entrega
        if taxa_entrega > 0:
            st.info(f"🛵 **Taxa de entrega para {bairro}:** R$ {taxa_entrega:.2f}")
        else:
            st.warning("⚠️ Taxa de entrega para este bairro será confirmada pelo WhatsApp.")
    else:
        st.info("🏪 **Retirada no Balcão:** Sem taxa de entrega.")

    st.write(f"## **Total Final: R$ {total_final:.2f}**")

    pagamento = st.selectbox(
        "Forma de Pagamento", ["Pix", "Cartão", "Dinheiro"]
    )

    pronto_para_enviar = False
    if tipo_entrega == "Entrega":
        if nome and rua_numero:
            pronto_para_enviar = True
    else:
        if nome:
            pronto_para_enviar = True

    if pronto_para_enviar:
        itens_txt = "\n".join(
            [f"{i['qtd']}x {i['item']} (R$ {i['subtotal']:.2f})" for i in carrinho]
        )

        if tipo_entrega == "Entrega":
            detalhes_tipo = f"*Tipo:* Entrega\n*Endereço:* {endereco}\n*Taxa de Entrega:* R$ {taxa_entrega:.2f}"
        else:
            detalhes_tipo = "*Tipo:* Retirada no Local"

        mensagem = (
            f"Olá! Gostaria de fazer um pedido na *Cuca Espetinhos e Lanches*:\n\n"
            f"*Cliente:* {nome}\n"
            f"{detalhes_tipo}\n"
            f"*Pagamento:* {pagamento}\n\n"
            f"*Itens:*\n{itens_txt}\n\n"
            f"*Total a Pagar:* R$ {total_final:.2f}"
        )

        numero_whatsapp = "5512992093751"

        # Botão para o usuário acionar o modal
        if st.button("🚀 AVANÇAR PARA CONFIRMAÇÃO", type="primary", use_container_width=True):
            st.session_state["mostrar_modal"] = True

        # Exibe o modal apenas quando ativado pelo session_state
        if st.session_state.get("mostrar_modal", False):
            modal_confirmacao(numero_whatsapp, mensagem)

    elif tipo_entrega == "Entrega" and not rua_numero:
        st.warning("Por favor, preencha o seu nome e informe a rua e número para liberar o pedido.")
    elif not nome:
        st.warning("Por favor, preencha o seu nome para liberar o pedido.")
