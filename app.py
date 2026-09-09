import urllib.parse
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Cuca Espetinhos e Lanches",
    page_icon="🍢",
    layout="centered"
)

# --- ESTILIZAÇÃO CSS (Botão WhatsApp grande e personalizado) ---
st.markdown("""
    <style>
    /* Estiliza os botões primários para se destacarem */
    div.stButton > button[kind="primary"], div.stLinkButton > a[kind="primary"] {
        width: 100% !important;
        height: 3.5em !important;
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #25D366 !important; /* Verde oficial do WhatsApp */
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div.stButton > button[kind="primary"]:hover, div.stLinkButton > a[kind="primary"]:hover {
        background-color: #1EBE5D !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Exibe o logo e título
st.image("logo.png", width=200)
st.title("🍢 Cuca Espetinhos e Lanches")

# Base de Dados do Cardápio
menu = {
    "X BURGER": {
        "preco": 19.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500"
    },
    "X SALADA": {
        "preco": 22.90,
        "imagem": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=500"
    },
    "ESPETINHO DE CARNE": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=500"
    }
}

# Inicializa o carrinho na sessão do Streamlit se ainda não existir
if "carrinho" not in st.session_state:
    st.session_state.carrinho = {}

# --- TELA DO CARDÁPIO ---
st.subheader("📋 Nosso Cardápio")

for item, info in menu.items():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image(info["imagem"], use_container_width=True)
    with col2:
        st.write(f"**{item}**")
        st.write(f"R$ {info['preco']:.2f}".replace('.', ','))
    with col3:
        if st.button(f"Adicionar", key=f"add_{item}"):
            st.session_state.carrinho[item] = st.session_state.carrinho.get(item, 0) + 1
            st.toast(f"{item} adicionado ao carrinho!", icon="🛒")
            st.rerun()

st.divider()

# --- DIÁLOGO DE CONFIRMAÇÃO DO PEDIDO (MODAL) ---
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, resumo_texto):
    st.write("Por favor, revise o seu pedido antes de ser direcionado ao WhatsApp:")
    st.info(resumo_texto)

    link_whatsapp = f"https://api.whatsapp.com/send?phone={numero_wa}&text={urllib.parse.quote(resumo_texto)}"

    st.write("---")
    col_voltar, col_enviar = st.columns([1, 2])

    with col_voltar:
        if st.button("❌ Alterar Pedido", use_container_width=True):
            st.rerun()

    with col_enviar:
        st.link_button(
            "📲 CONFIRMAR E ENVIAR",
            link_whatsapp,
            type="primary",
            use_container_width=True
        )

# --- RESUMO DO CARRINHO ---
st.subheader("🛒 Seu Carrinho")

if not st.session_state.carrinho:
    st.write("Seu carrinho está vazio.")
else:
    total_geral = 0.0
    resumo_itens_wa = []

    for item, qtd in list(st.session_state.carrinho.items()):
        preco_unitario = menu[item]["preco"]
        subtotal = preco_unitario * qtd
        total_geral += subtotal

        col_desc, col_qtd, col_del = st.columns([2, 1, 1])
        with col_desc:
            st.write(f"**{item}** (R$ {preco_unitario:.2f})")
        with col_qtd:
            st.write(f"Qtd: {qtd}")
        with col_del:
            if st.button("🗑️", key=f"rem_{item}"):
                del st.session_state.carrinho[item]
                st.rerun()

        resumo_itens_wa.append(f"• {qtd}x {item} - R$ {subtotal:.2f}".replace('.', ','))

    st.divider()
    st.markdown(f"### **Total: R$ {total_geral:.2f}**".replace('.', ','))

    # Número do WhatsApp do estabelecimento (com DDD e Código do País 55)
    NUMERO_WHATSAPP = "5512999999999"  # <--- Altere para o seu número real

    # Monta o texto para a mensagem do WhatsApp
    mensagem_final = (
        "Olá! Gostaria de fazer o seguinte pedido:\n\n"
        + "\n".join(resumo_itens_wa)
        + f"\n\n*Total: R$ {total_geral:.2f}*".replace('.', ',')
    )

    # Botão para abrir o fluxo de confirmação
    if st.button("🚀 AVANÇAR PARA CONFIRMAÇÃO", type="primary", use_container_width=True):
        modal_confirmacao(NUMERO_WHATSAPP, mensagem_final)
