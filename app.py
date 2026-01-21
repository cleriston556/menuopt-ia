import streamlit as st

st.set_page_config(page_title="MenuOpt IA", layout="wide")

st.title("📊 MenuOpt IA: Otimizador de Lucros para Delivery")
st.markdown("---")

# Formulário de Cadastro/Login Simples
with st.expander("🔑 Acesso do Restaurante"):
    nome = st.text_input("Nome do Restaurante")
    email = st.text_input("E-mail de contato")

# Área de Análise
col1, col2 = st.columns(2)

with col1:
    st.header("🛒 Adicionar Item")
    item = st.text_input("Nome do Prato (Ex: X-Salada)")
    custo = st.number_input("Custo de Produção (R$)", min_value=0.0)
    venda = st.number_input("Preço de Venda Atual (R$)", min_value=0.0)
    btn_analisar = st.button("Analisar Lucratividade")

with col2:
    st.header("💡 Sugestão da IA")
    if btn_analisar:
        lucro_bruto = venda - custo
        margem = (lucro_bruto / venda) * 100 if venda > 0 else 0
        
        st.metric("Margem Atual", f"{margem:.1f}%")
        
        if margem < 30:
            st.warning("⚠️ Atenção: Sua margem está abaixo do mercado (30%).")
            sugestao = custo / (1 - 0.35)
            st.success(f"📈 Sugestão: Reajuste para R$ {sugestao:.2f} para ter 35% de margem.")
        else:
            st.info("✅ Sua margem está saudável. Foque em combos para aumentar o ticket médio!")
