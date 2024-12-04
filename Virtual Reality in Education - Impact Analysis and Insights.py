import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from scipy import stats
from sklearn.preprocessing import LabelEncoder

# Veri Seti Yüklendi.
file_path = "C:\\Users\\LENOVO\\Desktop\\VR\\Virtual_Reality_in_Education_Impact.csv"  # Dosya yolunu güncelleyin
data = pd.read_csv(file_path)

# Grafiklerin kaydedileceği klasör
output_dir = "C:\\Users\\LENOVO\\Desktop\\VR\\Analysis_Results"  # Klasör yolunu güncelleyin
os.makedirs(output_dir, exist_ok=True)  # Klasörü oluştur (varsa bir şey yapmaz)

# 1. Tanımlayıcı İstatistik Analizi
# Yaş ve VR Kullanım Saatleri için özet istatistikler
age_stats = {
    'Mean': np.mean(data['Age']),
    'Median': np.median(data['Age']),
    'Mode': data['Age'].mode()[0]
}

vr_usage_stats = {
    'Min': np.min(data['Hours_of_VR_Usage_Per_Week']),
    'Max': np.max(data['Hours_of_VR_Usage_Per_Week']),
    'Std Dev': np.std(data['Hours_of_VR_Usage_Per_Week'])
}

# Kategorik Değişkenlerin Frekans Dağılımı
effectiveness_distribution = data['Perceived_Effectiveness_of_VR'].value_counts()

print("Age Statistics:", age_stats)
print("VR Usage Statistics:", vr_usage_stats)
print("Perceived Effectiveness of VR Distribution:")
print(effectiveness_distribution)

# 2. Keşifsel Veri Analizi (EDA)
# Histogram: Haftalık VR Kullanım Saatleri Dağılımı
plt.figure(figsize=(12, 6))
sns.histplot(data['Hours_of_VR_Usage_Per_Week'], bins=10, kde=True, color='skyblue')
plt.title('Weekly VR Usage Hours Distribution')
plt.xlabel('Hours of VR Usage per Week')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'weekly_vr_usage_distribution.png'))  # Grafik kaydedildi
plt.close()  # Grafiği kapat

# Kutu Grafiği: Stres Seviyesine Göre Haftalık VR Kullanımı
plt.figure(figsize=(12, 6))
sns.boxplot(x=data['Stress_Level_with_VR_Usage'], y=data['Hours_of_VR_Usage_Per_Week'], palette='Set3')
plt.title('Weekly VR Usage Hours by Stress Level')
plt.xlabel('Stress Level with VR Usage')
plt.ylabel('Hours of VR Usage per Week')
plt.savefig(os.path.join(output_dir, 'stress_level_vr_usage.png'))  # Grafik kaydedildi
plt.close()  # Grafiği kapat

# 3. Korelasyon Analizi
# Korelasyon Matrisi
correlations = data[['Hours_of_VR_Usage_Per_Week', 'Engagement_Level', 'Impact_on_Creativity',
                     'Perceived_Effectiveness_of_VR']].corr()

# Isı Haritası ile Korelasyon
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Analysis Heatmap')
plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))  # Grafik kaydedildi
plt.close()  # Grafiği kapat

# 4. Kategorik Veri Analizi
# Çapraz Tablolar: Bölge Bazında Improvement_in_Learning_Outcomes Analizi
cross_tab = pd.crosstab(data['Region'], data['Improvement_in_Learning_Outcomes'])
print("Bölge Bazında Improvement in Learning Outcomes Analizi:")
print(cross_tab)

# VR kullanan ve kullanmayan grupların Interest_in_Continuing_VR_Based_Learning oranlarının karşılaştırılması
vr_interest = pd.crosstab(data['Usage_of_VR_in_Education'], data['Interest_in_Continuing_VR_Based_Learning'])
print("\nVR Kullanımı ve İlgili Öğrenme Devam Etme İlgi Oranı:")
print(vr_interest)

# 5. Regresyon Analizi
# Perceived_Effectiveness_of_VR Değişkenini Tahmin Etme (Bağımlı Değişken)
# Bağımsız değişkenler: Hours_of_VR_Usage_Per_Week ve Instructor_VR_Proficiency
label_encoder = LabelEncoder()
data['Instructor_VR_Proficiency_Encoded'] = label_encoder.fit_transform(data['Instructor_VR_Proficiency'])

log_reg_model = LogisticRegression()
log_reg_model.fit(data[['Hours_of_VR_Usage_Per_Week', 'Instructor_VR_Proficiency_Encoded']], data['Improvement_in_Learning_Outcomes'])
log_reg_coeffs = pd.DataFrame(log_reg_model.coef_, columns=['Hours_of_VR_Usage_Per_Week', 'Instructor_VR_Proficiency_Encoded'], index=['Coef'])
print("\nLojistik Regresyon Katsayıları:")
print(log_reg_coeffs)

# 6. Segmentasyon ve Kümeleme (Clustering)

# K-means Kümeleme ile Segmentasyon
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(data[['Engagement_Level', 'Hours_of_VR_Usage_Per_Week', 'Impact_on_Creativity']])

plt.figure(figsize=(12, 6))
sns.scatterplot(x='Hours_of_VR_Usage_Per_Week', y='Impact_on_Creativity', hue='Cluster', data=data, palette='Set1')
plt.title('K-means Kümeleme Sonuçları')
plt.xlabel('Hours of VR Usage per Week')
plt.ylabel('Impact on Creativity')
plt.savefig(os.path.join(output_dir, 'kmeans_clustering_results.png'))  # Grafik kaydedildi
plt.close()  # Grafiği kapat

# 7. Hipotez Testleri

# t-testi: VR kullanan ve kullanmayan öğrencilerin Engagement_Level ortalamalarının anlamlı bir farkı olup olmadığı
vr_usage_group = data.groupby('Usage_of_VR_in_Education')['Engagement_Level']
t_stat, p_value = stats.ttest_ind(vr_usage_group.get_group('Yes'), vr_usage_group.get_group('No'))
print("\nt-test Sonuçları (Engagement Level):")
print(f"T-istatistiği: {t_stat}, p-değeri: {p_value}")

# Ki-kare testi: Stress_Level_with_VR_Usage ile Impact_on_Creativity arasında bağımlılık olup olmadığını incelemek
chi2_stat, p_val, dof, expected = stats.chi2_contingency(pd.crosstab(data['Stress_Level_with_VR_Usage'], data['Impact_on_Creativity']))
print("\nKi-kare Testi Sonuçları (Stress Level vs Impact on Creativity):")
print(f"Chi2 İstatistiği: {chi2_stat}, p-değeri: {p_val}")

