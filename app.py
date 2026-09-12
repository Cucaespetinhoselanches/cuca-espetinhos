import os
import html
import urllib.parse
import time
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cuca Espetinhos & Lanches", page_icon="🍢", layout="centered"
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

# ==================== FUNÇÕES CALLBACK E NAVEGAÇÃO ====================
def registrar_alteracao_item(chave_item, item_nome, preco):
    qtd = st.session_state.get(chave_item, 0)
    if qtd > 0:
        st.session_state["carrinho"][chave_item] = {
            "item": item_nome,
            "qtd": qtd,
            "subtotal": preco * qtd
        }
        st.session_state["ultimo_item_alterado"] = chave_item
    else:
        st.session_state["carrinho"].pop(chave_item, None)
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
        "<h3 style='color: #0f172a; font-weight: 800; font-size: 22px; margin-bottom: 15px;'>"
        "📋 Revise os detalhes do seu pedido:"
        "</h3>",
        unsafe_allow_html=True,
    )
    
    mensagem_html = html.escape(mensagem_texto).replace("\n", "<br>")
    st.markdown(
        f"""
        <div style='background-color: #ffffff; padding: 16px; border-radius: 8px; border: 2px solid #cbd5e1; font-size: 18px; line-height: 1.5; color: #0f172a; font-weight: 500;'>
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

# ==================== ESTILIZAÇÃO CSS CUSTOMIZADA ====================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    /* Fundo Global e Fonte */
    html, body, [class*="css"], .stApp {
        background-color: #f8fafc !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
        color: #0f172a !important;
    }

    header {visibility: hidden;}

    /* Banner Principal */
    .hero-banner {
        background: linear-gradient(135deg, #7f1d1d 0%, #991b1b 100%);
        border-radius: 12px;
        padding: 22px 20px;
        color: #ffffff;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 0.08em;
        color: #fca5a5;
        text-transform: uppercase;
        margin-bottom: 4px;
    }

    .hero-title {
        font-size: 32px;
        font-weight: 900;
        line-height: 1.1;
        color: #ffffff;
        margin: 0;
    }

    .info-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: space-between;
        background: #ffffff;
        padding: 12px 16px;
        border-radius: 8px;
        border: 2px solid #cbd5e1;
        font-size: 15px;
        color: #0f172a;
        font-weight: 700;
        margin-bottom: 20px;
    }

    /* Abas de Categoria com Fonte Grande */
    button[data-baseweb="tab"] {
        font-size: 18px !important;
        font-weight: 800 !important;
        background-color: transparent !important;
        color: #475569 !important;
        border: none !important;
        border-bottom: 4px solid transparent !important;
        padding: 10px 16px !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #dc2626 !important;
        border-bottom: 4px solid #dc2626 !important;
    }

    .section-header {
        font-size: 20px;
        font-weight: 900;
        letter-spacing: 0.04em;
        color: #0f172a;
        text-transform: uppercase;
        margin-top: 12px;
        margin-bottom: 14px;
        border-bottom: 2px solid #cbd5e1;
        padding-bottom: 6px;
    }

    /* MINIATURA MICRO (24px x 24px) */
    .thumb-mini {
        width: 24px !important;
        height: 24px !important;
        max-width: 24px !important;
        max-height: 24px !important;
        min-width: 24px !important;
        min-height: 24px !important;
        object-fit: cover !important;
        border-radius: 4px !important;
        vertical-align: middle !important;
        display: inline-block !important;
        margin-right: 8px !important;
    }

    /* CARD DO ITEM */
    .menu-item-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 14px;
        border: 2px solid #cbd5e1;
        margin-bottom: 8px;
    }

    /* TEXTOS GRANDES DOS PRODUTOS */
    .item-title {
        font-size: 22px !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        flex-wrap: wrap;
    }

    .item-desc {
        color: #334155 !important;
        font-size: 16px !important;
        line-height: 1.4 !important;
        margin-bottom: 8px !important;
        font-weight: 500 !important;
    }

    .badge-mais-pedido {
        background-color: #fef2f2;
        color: #dc2626;
        border: 1px solid #fecaca;
        font-size: 13px;
        font-weight: 800;
        padding: 2px 8px;
        border-radius: 6px;
        display: inline-block;
        margin-left: 8px;
        vertical-align: middle;
    }

    .preco-badge {
        color: #047857 !important;
        font-weight: 900 !important;
        font-size: 22px !important;
        display: inline-block;
        margin-bottom: 6px;
    }

    /* INPUTS DE QUANTIDADE */
    div[data-testid="stNumberInput"] input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 2px solid #64748b !important;
        font-weight: 800 !important;
        font-size: 20px !important;
        height: 46px !important;
    }

    /* BOTÕES MAIORES E MAIS NÍTIDOS */
    div.stButton > button, 
    div.stButton > button *,
    div.stLinkButton > a,
    div.stLinkButton > a * {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 2px solid #475569 !important;
        border-radius: 8px !important;
        font-weight: 800 !important;
        font-size: 17px !important;
    }

    div.stButton > button:hover {
        background-color: #f1f5f9 !important;
    }

    div.stButton > button[kind="primary"], 
    div.stButton > button[kind="primary"] *,
    div.stLinkButton > a[kind="primary"],
    div.stLinkButton > a[kind="primary"] * {
        background-color: #dc2626 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 900 !important;
        font-size: 18px !important;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #b91c1c !important;
    }

    label {
        font-size: 17px !important;
        font-weight: 800 !important;
        color: #0f172a !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==================== CABEÇALHO SUPERIOR ====================
st.markdown(
    """
    <div style='display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-bottom: 2px solid #cbd5e1; margin-bottom: 14px;'>
        <div style='display: flex; align-items: center; gap: 10px;'>
            <div style='background: #dc2626; padding: 6px 12px; border-radius: 8px; color: white; font-weight: bold; font-size: 22px;'>🍢</div>
            <div>
                <h2 style='margin: 0; font-size: 22px; font-weight: 900; color: #0f172a;'>CUCA</h2>
                <p style='margin: 0; font-size: 12px; font-weight: 800; color: #64748b; letter-spacing: 0.04em;'>ESPETINHOS & LANCHES</p>
            </div>
        </div>
        <div>
            <span style='background: #ecfdf5; color: #047857; font-size: 14px; font-weight: 800; padding: 6px 12px; border-radius: 12px; border: 1px solid #a7f3d0;'>• Aberto agora</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-banner">
        <div class="hero-subtitle">NA BRASA, FEITO NA HORA</div>
        <div class="hero-title">Espetinho<br>da Cuca</div>
    </div>
    <div class="info-bar">
        <span>🕒 Entrega 30–45 min</span>
        <span>🛵 Taxa R$ 3,00 a R$ 8,00</span>
        <span>💵 Pedido min. R$ 20,00</span>
        <span>🏪 Retirada no balcão</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==================== CARDÁPIO / MENU ====================
menu_categorias = {
    "Espetos": {
        "Espeto Pão de Alho": {
            "preco": 9.00,
            "descricao": "Pão artesanal no alho e manteiga, tostado na brasa até dourar.",
            "mais_pedido": True,
            "imagem": "https://casadecarnesdomaninho.com.br/wp-content/uploads/2022/06/espetinho-pao-de-alho.jpg",
        },
        "Espeto Queijo Coalho": {
            "preco": 9.00,
            "descricao": "Queijo coalho tostado por fora e derretido por dentro.",
            "mais_pedido": False,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpyXQSm25u3do9kGas7sKk1Lf1oXX7mcrS5IC9w5UPKUfGRAdrjq2a8vFs&s=10",
        },
        "Espeto Alcatra": {
            "preco": 12.00,
            "descricao": "Corte de alcatra macia e suculenta assada na brasa.",
            "mais_pedido": True,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "Espeto Picanha": {
            "preco": 18.00,
            "descricao": "Picanha nobre com camada leve de gordura.",
            "mais_pedido": True,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
        "Espeto Frango": {
            "preco": 12.00,
            "descricao": "Peito de frango temperado no ponto certo.",
            "mais_pedido": False,
            "imagem": "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg",
        },
    },
    "Lanches": {
        "X Burger": {
            "preco": 19.90,
            "descricao": "Hambúrguer artesanal, queijo derretido e maionese da casa.",
            "mais_pedido": False,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800",
        },
        "X Salada": {
            "preco": 29.90,
            "descricao": "Hambúrguer artesanal, queijo, alface, tomate e maionese.",
            "mais_pedido": True,
            "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800",
        },
    },
    "Porções": {
        "Porção Batata Frita": {
            "preco": 29.90,
            "descricao": "Batata frita crocante por fora e macia por dentro.",
            "mais_pedido": True,
            "imagem": "https://2.bp.blogspot.com/-zNkU0qa51Uk/U5elL6RgI6I/AAAAAAAAACo/OngayLy9ogk/s1600/batata.jpg",
        },
    },
    "Refrigerantes": {
        "Coca-Cola Lata 350ml": {
            "preco": 6.00,
            "descricao": "Lata 350ml gelada.",
            "mais_pedido": True,
            "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
        },
    },
    "Cervejas": {
        "Cerveja Original 300ml": {
            "preco": 6.00,
            "descricao": "Garrafinha 300ml trincando.",
            "mais_pedido": True,
            "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRllDI7RJyBsZMII0SR2UZhiYstauUqjyhKbGznH27HEw&s=10",
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

abas = st.tabs(list(menu_categorias.keys()))

for aba, (categoria, itens) in zip(abas, menu_categorias.items()):
    with aba:
        st.markdown(f"<div class='section-header'>{categoria.upper()} NA BRASA</div>", unsafe_allow_html=True)
        for item, info in itens.items():
            chave_item = f"{categoria}_{item}"
            badge = "<span class='badge-mais-pedido'>Mais pedido</span>" if info.get("mais_pedido") else ""
            
            st.markdown(
                f"""
                <div class='menu-item-box'>
                    <div class='item-title'>
                        <img class='thumb-mini' src='{info['imagem']}' alt='{item}'>
                        <span>{item}</span>
                        {badge}
                    </div>
                    <div class='item-desc'>{info.get('descricao', '')}</div>
                    <div class='preco-badge'>R$ {info['preco']:.2f}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            qtd = st.number_input(
                "Qtd:",
                min_value=0,
                max_value=20,
                step=1,
                key=chave_item,
                label_visibility="collapsed",
                on_change=registrar_alteracao_item,
                args=(chave_item, item, info["preco"]),
            )

            if (
                st.session_state.get("ultimo_item_alterado") == chave_item
                and qtd > 0
                and st.session_state["etapa_pedido"] == "cardapio"
            ):
                st.success(f"✅ **{qtd}x {item}** adicionado ao carrinho!")
                col_mais, col_encerrar = st.columns(2)
                with col_mais:
                    st.button("➕ Adicionar Mais", key=f"btn_mais_{chave_item}", use_container_width=True, on_click=continuar_comprando)
                with col_encerrar:
                    st.button("✅ Finalizar Pedido", key=f"btn_encerrar_{chave_item}", type="primary", use_container_width=True, on_click=avancar_para_entrega)

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
            <div style='background-color: #ecfdf5; border-left: 6px solid #10b981; padding: 16px; border-radius: 8px; margin-bottom: 15px;'>
                <p style='color: #065f46 !important; font-size: 17px !important; margin-bottom: 2px;'>📱 <b>Chave PIX (Telefone):</b></p>
                <p style='color: #047857 !important; font-size: 26px !important; font-weight: 900 !important; margin: 0;'>{CHAVE_PIX_VAL}</p>
                <p style='color: #334155 !important; font-size: 14px !important; margin-top: 4px;'><i>Por favor, envie o comprovante pelo WhatsApp após finalizar o pedido.</i></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

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

    texto_pagamento = f"Pix (Chave: {CHAVE_PIX_VAL})" if pagamento == "Pix" else pagamento

    mensagem = (
        f"Olá! Gostaria de fazer um pedido na *Cuca Espetinhos & Lanches*:\n\n"
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

    # ROLAGEM AUTOMÁTICA
    components.html(
        """
        <script>
            function rolarAteEntrega() {
                var el = window.parent.document.getElementById('secao-entrega');
                if (el) {
                    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                } else {
                    setTimeout(rolarAteEntrega, 100);
                }
            }
            setTimeout(rolarAteEntrega, 200);
        </script>
        """,
        height=0,
    )
