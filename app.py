import urllib.parse
import streamlit as st
import streamlit.components.v1 as components  # Import para rodar o JavaScript

# ==================== ESTADOS DA SESSÃO ====================
if "mostrar_modal" not in st.session_state:
    st.session_state["mostrar_modal"] = False

if "etapa_pedido" not in st.session_state:
    st.session_state["etapa_pedido"] = "cardapio"

if "ultimo_item_alterado" not in st.session_state:
    st.session_state["ultimo_item_alterado"] = None

# Callback Functions
def registrar_alteracao_item(nome_item):
    if st.session_state.get(nome_item, 0) > 0:
        st.session_state["ultimo_item_alterado"] = nome_item

def avancar_para_entrega():
    st.session_state["etapa_pedido"] = "dados_entrega"

def continuar_comprando():
    st.session_state["ultimo_item_alterado"] = None
    st.session_state["etapa_pedido"] = "cardapio"

# ==================== MODAL DE CONFIRMAÇÃO ====================
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, mensagem_texto):
    st.markdown(
        "<h3 style='color: #000000; font-weight: 800; margin-bottom: 15px;'>"
        "📋 Revise os detalhes do seu pedido:"
        "</h3>",
        unsafe_allow_html=True,
    )
    st.info(mensagem_texto)

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

# =======================================================================

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

# Estilização CSS
st.markdown(
    """
    <style>
    label, div[data-testid="stMarkdownContainer"] p {
        font-size: 18px !important;
    }

    h1 { font-size: 32px !important; }
    h2 { font-size: 26px !important; }
    h3 { font-size: 22px !important; }

    .preco-destaque {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #2e7d32 !important;
    }

    div.stButton > button {
        font-size: 18px !important;
        font-weight: bold !important;
        min-height: 3em !important;
        border-radius: 10px !important;
    }

    div.stLinkButton > a[kind="primary"], div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 3.5em !important;
        background-color: #25D366 !important;
        border: none !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    div.stLinkButton > a[kind="primary"] p, div.stButton > button[kind="primary"] p {
        font-size: 22px !important;
        font-weight: 900 !important;
        color: #0b3d18 !important;
    }
    
    div[data-testid="stNotification"] {
        background-color: #e3f2fd !important;
        border-left-color: #0d47a1 !important;
    }

    div[data-testid="stNotification"] p {
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #000000 !important;
        line-height: 1.6 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.image("logo.png", width=200)
st.title("🍢 Cuca Espetinhos e Lanches")

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
    "HOT CALABRESA": {
        "preco": 16.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "Refrigerante Lata": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    },
}

taxas_bairros = {
    "Nova Jacareí": 3.00,
    "Igarapés": 5.00,
    "Esperança": 4.00,
    "Centro": 8.00,
    "Outro Bairro (A combinar)": 0.00,
}

carrinho = []
subtotal_produtos = 0.0

st.subheader("Faça seu Pedido")

# Exibe o cardápio
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
            label_visibility="collapsed",
            on_change=registrar_alteracao_item,
            args=(item,),
        )
        if qtd > 0:
            subtotal_item = info["preco"] * qtd
            carrinho.append(
                {"item": item, "qtd": qtd, "subtotal": subtotal_item}
            )
            subtotal_produtos += subtotal_item

    # Pergunta exibida logo abaixo do item selecionado
    if (
        st.session_state.get("ultimo_item_alterado") == item
        and qtd > 0
        and st.session_state["etapa_pedido"] == "cardapio"
    ):
        st.info(f"✅ **{qtd}x {item}** adicionado ao pedido!")
        st.markdown("**Deseja inserir mais produtos ou encerrar o pedido?**")

        col_mais, col_encerrar = st.columns(2)
        with col_mais:
            st.button(
                "➕ Inserir mais produtos",
                key=f"btn_mais_{item}",
                use_container_width=True,
                on_click=continuar_comprando,
            )

        with col_encerrar:
            st.button(
                "✅ Encerrar pedido",
                key=f"btn_encerrar_{item}",
                type="primary",
                use_container_width=True,
                on_click=avancar_para_entrega,
            )

        st.write("---")

# ==================== DADOS DE ENTREGA E PAGAMENTO ====================
if carrinho and st.session_state["etapa_pedido"] == "dados_entrega":
    # ÂNCORA PARA A ROLAGEM AUTOMÁTICA
    st.markdown("<div id='secao-entrega'></div>", unsafe_allow_html=True)

    st.divider()
    st.subheader("📦 Dados de Entrega e Pagamento")
    st.write(f"### **Subtotal dos itens: R$ {subtotal_produtos:.2f}**")

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
        bairro = st.selectbox(
            "Selecione o seu Bairro:", list(taxas_bairros.keys())
        )
        taxa_entrega = taxas_bairros[bairro]
        rua_numero = st.text_input("Rua e Número:")

        if rua_numero:
            endereco = f"{rua_numero} - {bairro}"

        total_final += taxa_entrega
        if taxa_entrega > 0:
            st.info(
                f"🛵 **Taxa de entrega para {bairro}:** R$ {taxa_entrega:.2f}"
            )
        else:
            st.warning(
                "⚠️ Taxa de entrega para este bairro será confirmada pelo WhatsApp."
            )
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
            [
                f"{i['qtd']}x {i['item']} (R$ {i['subtotal']:.2f})"
                for i in carrinho
            ]
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

        if st.button(
            "🚀 AVANÇAR PARA CONFIRMAÇÃO",
            type="primary",
            use_container_width=True,
        ):
            st.session_state["mostrar_modal"] = True

        if st.session_state.get("mostrar_modal", False):
            modal_confirmacao(numero_whatsapp, mensagem)

    elif tipo_entrega == "Entrega" and not rua_numero:
        st.warning("Por favor, informe seu nome, rua e número para enviar.")
    elif not nome:
        st.warning("Por favor, preencha o seu nome para liberar o pedido.")

    # JAVASCRIPT: Executa o rolamento automático suave para a seção de entrega
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
