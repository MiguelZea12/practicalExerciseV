import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def crear_visualizaciones(df):
    fig, axs = plt.subplots(2, 2, figsize=(16, 14))
    fig.subplots_adjust(hspace=0.5, wspace=0.9)

    # Gráfico 1: Distribución de la Depresión según el Género
    depresion_genero = df.groupby(['Gender', 'Depression']).size().unstack(fill_value=0)
    depresion_genero = depresion_genero.div(depresion_genero.sum(axis=1), axis=0) * 100
    depresion_genero.plot(kind='barh', stacked=True, ax=axs[0, 0], color=['#ff9999', '#66b3ff'])
    axs[0, 0].set_title('Distribución de la Depresión según el Género', fontsize=14, fontweight='bold')
    axs[0, 0].set_xlabel('Porcentaje (%)', fontsize=12)
    axs[0, 0].set_ylabel('Género', fontsize=12)
    axs[0, 0].legend(title='Depresión', labels=['No', 'Sí'], fontsize=10)

    # Gráfico 2: Relación entre la Presión Académica y la Duración del Sueño
    sns.boxplot(data=df, x='Academic Pressure', y='Sleep Duration', ax=axs[0, 1])
    axs[0, 1].set_title('Distribución de Sueño según Presión Académica', fontsize=14)
    axs[0, 1].set_xlabel('Presión Académica', fontsize=12)
    axs[0, 1].set_ylabel('Duración del Sueño (Horas)', fontsize=12)

    # Gráfico 3: Porcentaje de personas con pensamientos suicidas según antecedentes familiares
    pensamientos_suicidas_antecedentes_familiares = df.groupby(['Have you ever had suicidal thoughts ?', 'Family History of Mental Illness']).size().unstack(fill_value=0)
    pensamientos_suicidas_antecedentes_familiares_porcentaje = pensamientos_suicidas_antecedentes_familiares.div(pensamientos_suicidas_antecedentes_familiares.sum(axis=1), axis=0) * 100
    pensamientos_suicidas_antecedentes_familiares_porcentaje['Yes'].plot.pie(ax=axs[1, 0], autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white'})
    axs[1, 0].set_title('Impacto de los antecedentes familiares en los pensamientos suicidas', fontsize=14, fontweight='bold')
    axs[1, 0].set_ylabel('', fontsize=12)

    # Gráfico 4: Evolución del CGPA en función de la Satisfacción con los Estudios
    sns.lineplot(data=df, x='Study Satisfaction', y='CGPA', marker='o', ax=axs[1, 1])
    axs[1, 1].set_title('Evolución del CGPA en función de la Satisfacción con los Estudios', fontsize=14, fontweight='bold')
    axs[1, 1].set_xlabel('Satisfacción con los Estudios', fontsize=12)
    axs[1, 1].set_ylabel('CGPA', fontsize=12)
    axs[1, 1].grid(True)

    plt.show()
