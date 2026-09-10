import os
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

if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = {}

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

# --- ESTILIZAÇÃO CSS CUSTOMIZADA (DARK MODE + ABAS + LOGO INTEIRA SEM CORTE) ---
st.markdown(
    """
    <style>
    /* FUNDO ESCURO (DARK MODE) */
    .stApp {
        background-color: #0f172a !important;
        color: #f8fafc !important;
    }

    /* TÍTULOS PRINCIPAIS */
    h1 {
        font-size: 32px !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 5px !important;
    }

    /* FOTO/LOGO DO BAR - INTEIRA SEM CORTE */
    div[data-testid="stImage"] img {
        max-height: none !important;
        height: auto !important;
        width: 100% !important;
        object-fit: contain !important;
    }

    div[data-testid="stImage"] > div {
        max-height: none !important;
        height: auto !important;
    }

    /* CARDS DOS PRODUTOS EM TOM ESCURO DESTACADO */
    div[data-testid="stColumn"] > div {
        background-color: #1e293b !important;
        border-radius: 16px;
        padding: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        border: 1px solid #334155 !important;
        margin-bottom: 10px;
    }

    /* RÓTULOS E TEXTOS DE INPUTS */
    label, p, span, div {
        color: #f8fafc !important;
    }

    /* DESTAQUE GRANDE PARA AS ABAS */
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

    /* Aba Selecionada */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #ef4444 !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
    }

    /* PREÇO GRANDE E DESTACADO */
    .preco-badge {
        background-color: #15803d !important;
        color: #ffffff !important;
        font-weight: 900;
        font-size: 24px !important;
        padding: 4px 12px;
        border-radius: 8px;
        display: inline-block;
        margin-top: 6px;
        margin-bottom: 6px;
    }

    /* DESTAQUE PARA O CAMPO DE QUANTIDADE (NUMBER INPUT) */
    div[data-testid="stNumberInput"] input {
        font-size: 22px !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        text-align: center !important;
        height: 48px !important;
    }

    div[data-testid="stNumberInput"] button {
        height: 48px !important;
        width: 48px !important;
        background-color: #334155 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }

    /* BOTÕES COM ALTO CONTRASTE */
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

    /* NOTIFICAÇÃO INLINE */
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

    /* CAMPOS DE TEXTO / SELEÇÃO */
    div[data-baseweb="input"] input, div[data-baseweb="select"] {
        background-color: #0f172a !important;
        color: #ffffff !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==================== CARREGAMENTO SEGURO DA LOGO ====================
# Procura automaticamente variações do arquivo na pasta do projeto
opcoes_logo = [
    "logo.png", "logo.jpg", "logo.jpeg", "logo.webp",
    "Logo.png", "Logo.jpg", "LOGO.PNG", "LOGO.JPG"
]

logo_encontrada = None
for nome_arquivo in opcoes_logo:
    if os.path.exists(nome_arquivo):
        logo_encontrada = nome_arquivo
        break

if logo_encontrada:
    st.image(logo_encontrada, use_container_width=True)
else:
    st.warning("⚠️ O arquivo da logo não foi localizado na raiz do repositório.")

st.title("🍢 Cuca Espetinhos e Lanches")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 16px; margin-bottom: 25px;'>Monte seu pedido de forma rápida e prática</p>", unsafe_allow_html=True)

menu_categorias = {
    "🍢 Espetos": {
        "ESPETO PÃO DE ALHO ou QUEIJO COALHO ou LINGUIÇA": {
            "preco": 9.00,
            "imagem": "https://i.pinimg.com/474x/ca/88/97/ca8897789a429b07bc7a9f238c348223.jpg",
        },
        "ESPETO ROMEU E JULIETA (Bacon/Goiabada/Queijo)": {
            "preco": 15.00,
            "imagem": "https://media.istockphoto.com/id/1270859209/pt/foto/kebab-grilled-meat-on-a-cutting-board-with-flour-and-vinaigrette-salad.jpg?s=612x612&w=0&k=20&c=K50axpMgL8NejcoLFl_HV8RI5hIKOgjPJ7AKqSsFcAk=",
        },
        "ESPETO PANCETA ou ALCATRA ou FRALDINHA ou KAFTA ou FRANGO": {
            "preco": 12.00,
            "imagem": "https://media.istockphoto.com/id/1270859209/pt/foto/kebab-grilled-meat-on-a-cutting-board-with-flour-and-vinaigrette-salad.jpg?s=612x612&w=0&k=20&c=K50axpMgL8NejcoLFl_HV8RI5hIKOgjPJ7AKqSsFcAk=",
        },
        "ESPETO PICANHA ou CORAÇÃO": {
            "preco": 18.00,
            "imagem": "https://media.istockphoto.com/id/1270859209/pt/foto/kebab-grilled-meat-on-a-cutting-board-with-flour-and-vinaigrette-salad.jpg?s=612x612&w=0&k=20&c=K50axpMgL8NejcoLFl_HV8RI5hIKOgjPJ7AKqSsFcAk=",
        },
    },
    "🥪 Lanches": {
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
    },
    "🍟 Porções": {
        "PORÇÃO BATATA FRITA ou PORÇÃO DE MANDIOCA FRITA": {
            "preco": 29.90,
            "imagem": "https://plus.unsplash.com/premium_photo-1672774750509-bc9ff226f3e8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cG9yJUMzJUE3JUMzJUE3byUyMGJhdGF0YSUyMGZyaXRhfGVufDB8fDB8fHww",
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

# ==================== EXIBIÇÃO DO CARDÁPIO ====================
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
                    st.session_state["carrinho"][chave_item] = {
                        "item": item,
                        "qtd": qtd,
                        "subtotal": info["preco"] * qtd
                    }

            # Alerta e Botões Inline abaixo do último item alterado
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

# Obter itens do carrinho permanente
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

    # Prepara a mensagem para envio
    itens_txt = "\n".join(
        [
            f"{i['qtd']}x {i['item']} (R$ {i['subtotal']:.2f})"
            for i in itens_carrinho
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
        if tipo_entrega == "Entrega" and not rua_numero.strip():
            st.error("Por favor, preencha a Rua e o Número para continuar.")
        elif not nome.strip():
            st.error("Por favor, informe seu nome para continuar.")
        else:
            st.session_state["mostrar_modal"] = True

    if st.session_state.get("mostrar_modal", False):
        modal_confirmacao(numero_whatsapp, mensagem)

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
