import urllib.parse
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

# ==================== ESTADOS DA SESSÃO ====================
if "mostrar_modal" not in st.session_state:
    st.session_state["mostrar_modal"] = False

if "etapa_pedido" not in st.session_state:
    st.session_state["etapa_pedido"] = "cardapio"

if "ultimo_item_alterado" not in st.session_state:
    st.session_state["ultimo_item_alterado"] = None

# Funções Callback
def registrar_alteracao_item(chave_item):
    if st.session_state.get(chave_item, 0) > 0:
        st.session_state["ultimo_item_alterado"] = chave_item

def avancar_para_entrega():
    st.session_state["etapa_pedido"] = "dados_entrega"

def continuar_comprando():
    st.session_state["ultimo_item_alterado"] = None
    st.session_state["etapa_pedido"] = "cardapio"

# ==================== MODAL DE CONFIRMAÇÃO ====================
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, mensagem_texto):
    st.markdown(
        "<h3 style='color: #1a1a1a; font-weight: 800; margin-bottom: 15px;'>"
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

# --- ESTILIZAÇÃO CSS CUSTOMIZADA ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f9fa;
    }

    h1 {
        font-size: 30px !important;
        font-weight: 800 !important;
        color: #1e293b !important;
        text-align: center;
        margin-bottom: 5px !important;
    }

    div[data-testid="stColumn"] > div {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
        border: 1px solid #f1f5f9;
        margin-bottom: 10px;
    }

    div[data-testid="stImage"] img {
        max-height: 85px !important;
        object-fit: cover !important;
        border-radius: 10px !important;
    }

    .preco-badge {
        background-color: #e8f5e9;
        color: #1b5e20;
        font-weight: 900;
        font-size: 24px !important;
        padding: 4px 12px;
        border-radius: 8px;
        display: inline-block;
        margin-top: 6px;
        margin-bottom: 6px;
    }

    button[data-baseweb="tab"] {
        font-size: 16px !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        padding: 8px 16px !important;
    }

    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }

    div.stButton > button[kind="primary"], div.stLinkButton > a[kind="primary"] {
        background-color: #25D366 !important;
        border: none !important;
        border-radius: 12px !important;
    }

    div.stButton > button[kind="primary"] p, div.stLinkButton > a[kind="primary"] p {
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 18px !important;
    }

    div[data-testid="stNotification"] {
        background-color: #f0fdf4 !important;
        border-left: 5px solid #22c55e !important;
        border-radius: 12px !important;
    }
    div[data-testid="stNotification"] p {
        color: #15803d !important;
        font-size: 16px !important;
        font-weight: 600 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

col_center = st.columns([1, 2, 1])
with col_center[1]:
    st.image("logo.png", use_container_width=True)

st.title("🍢 Cuca Espetinhos e Lanches")
st.markdown("<p style='text-align: center; color: #64748b; font-size: 16px; margin-bottom: 25px;'>Monte seu pedido de forma rápida e prática</p>", unsafe_allow_html=True)

menu_categorias = {
    "🥪 Lanches": {
        "X BURGER": {
            "preco": 19.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60",
        },
        "X SALADA": {
            "preco": 29.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60",
        },
        "X BACON": {
            "preco": 35.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60",
        },
        "HOT CALABRESA": {
            "preco": 16.50,
            "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60",
        },
    },
    "🍟 Porções": {
        "Batata Frita Tradicional": {
            "preco": 22.00,
            "imagem": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500&auto=format&fit=crop&q=60",
        },
        "Batata com Bacon e Queijo": {
            "preco": 32.00,
            "imagem": "https://images.unsplash.com/photo-1585109649139-366815a0d713?w=500&auto=format&fit=crop&q=60",
        },
    },
    "🥤 Refrigerantes": {
        "Refrigerante Lata 350ml": {
            "preco": 6.00,
            "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
        },
        "Refrigerante 2 Litros": {
            "preco": 12.00,
            "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
        },
    },
    "🍺 Cervejas": {
        "Cerveja Lata 350ml": {
            "preco": 7.50,
            "imagem": "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=400",
        },
        "Cerveja Long Neck": {
            "preco": 10.00,
            "imagem": "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=400",
        },
    },
}

taxas_bairros = {
    "Nova Jacareí": 3.00,
    "Igarapés": 5.00,
    "Esperança": 4.00,
    "Centro": 8.00,
    "Outro Bairro (A combinar)": 0.00,
}

# MONTAR CARRINHO PERMANENTE NA SESSÃO
carrinho = []
subtotal_produtos = 0.0

abas = st.tabs(list(menu_categorias.keys()))

for aba, (categoria, itens) in zip(abas, menu_categorias.items()):
    with aba:
        for item, info in itens.items():
            chave_item = f"{categoria}_{item}"
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(info["imagem"], use_container_width=True)
            with col2:
                st.markdown(f"**{item}**")
                st.markdown(f"<span class='preco-badge'>R$ {info['preco']:.2f}</span>", unsafe_allow_html=True)
                
                qtd = st.number_input(
                    "Qtd:",
                    min_value=0,
                    step=1,
                    key=chave_item,
                    label_visibility="collapsed",
                    on_change=registrar_alteracao_item,
                    args=(chave_item,),
                )
                
            if qtd > 0:
                subtotal_item = info["preco"] * qtd
                carrinho.append(
                    {"item": item, "qtd": qtd, "subtotal": subtotal_item}
                )
                subtotal_produtos += subtotal_item

            # Exibe confirmação no item alterado
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

# ==================== DADOS DE ENTREGA E PAGAMENTO ====================
if carrinho and st.session_state["etapa_pedido"] == "dados_entrega":
    st.markdown("<div id='secao-entrega'></div>", unsafe_allow_html=True)

    st.write("---")
    st.subheader("📦 Entrega & Pagamento")
    st.markdown(f"### Subtotal: **R$ {subtotal_produtos:.2f}**")

    nome = st.text_input("Seu Nome:", key="input_nome")
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
        bairro = st.selectbox(
            "Selecione o Bairro:", list(taxas_bairros.keys()), key="input_bairro"
        )
        taxa_entrega = taxas_bairros[bairro]
        rua_numero = st.text_input("Rua e Número:", key="input_rua")

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

    pagamento = st.selectbox(
        "Forma de Pagamento", ["Pix", "Cartão", "Dinheiro"], key="input_pagamento"
    )

    # Validação do preenchimento
    pronto_para_enviar = False
    if tipo_entrega == "Entrega":
        if nome.strip() and rua_numero.strip():
            pronto_para_enviar = True
    else:
        if nome.strip():
            pronto_para_enviar = True

    if pronto_para_enviar:
        itens_txt = "\n".join(
            [
                f"{i['qtd']}x {i['item']} (R$ {i['subtotal']:.2f})"
                for i in carrinho
            ]
        )

        if tipo_entrega == "Entrega":
            detalhes_tipo = f"*Tipo:* Entrega\n*Endereço:* {endereco}\n*Taxa:* R$ {taxa_entrega:.2f}"
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
            key="btn_avancar_confirmacao"
        ):
            st.session_state["mostrar_modal"] = True

        if st.session_state.get("mostrar_modal", False):
            modal_confirmacao(numero_whatsapp, mensagem)

    elif tipo_entrega == "Entrega" and not rua_numero.strip():
        st.warning("Por favor, preencha o endereço completo para liberar o botão de confirmação.")
    elif not nome.strip():
        st.warning("Por favor, informe seu nome para liberar o botão de confirmação.")

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
