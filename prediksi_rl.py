import pickle
import streamlit as st

model = pickle.load(open('best_model_rbf.sav', 'rb'))

st.title('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii di Desa Lontar')

tahun = st.number_input('Input Tahun Prediksi')
bulan = st.number_input('Input Bulan Prediksi')
tanggal = st.number_input('Input Tanggal Prediksi')
arus = st.number_input('Input Arus Prediksi')
salinitas = st.number_input('Input Salinitas Prediksi')
suhu = st.number_input('Input Suhu Prediksi')
harga_bibit = st.number_input('Input Harga Bibit Prediksi')
modal = st.number_input('Input Modal Prediksi')

predict = ''

if st.button ('Prediksi'):
    predict = model.predict(
        [[tahun,bulan,tanggal,arus,salinitas,suhu,harga_bibit,modal]]
    )
    st.write('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii : ', predict)