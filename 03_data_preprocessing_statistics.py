"""Data preprocessing and statistics assignment solutions.
Optional dependencies: pandas, numpy, matplotlib, scikit-learn, scipy.
Dataset filenames are placeholders; place your CSV files beside this script or pass their paths.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder

def iris_species_pie(path="iris.csv"):
    df=pd.read_csv(path)
    col="Species" if "Species" in df.columns else "species"
    df[col].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
    plt.title("Iris species distribution"); plt.ylabel(""); plt.tight_layout(); plt.show()

def describe_dataset(path):
    df=pd.read_csv(path)
    print("Shape:",df.shape); print("Columns:",df.columns.tolist()); print("Dtypes:\n",df.dtypes)
    print("Description:\n",df.describe(include="all")); print("First 3 rows:\n",df.head(3))
    return df

def fill_salary_age_means(path="Data.csv"):
    df=pd.read_csv(path)
    for col in ("salary","age"):
        if col in df.columns: df[col]=df[col].fillna(df[col].mean())
    return df

def name_salary_line(path):
    df=pd.read_csv(path)
    df.plot(x="Name",y="Salary",kind="line",marker="o",legend=False)
    plt.xticks(rotation=45,ha="right"); plt.tight_layout(); plt.show()

def iris_boxplots(path="iris.csv"):
    df=pd.read_csv(path)
    features=[c for c in ["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm",
                          "sepal_length","sepal_width","petal_length","petal_width"] if c in df.columns]
    species_col=next((c for c in ["Species","species"] if c in df.columns),None)
    if not features: raise ValueError("No known Iris feature columns found")
    df[features].plot(kind="box",subplots=True,layout=(2,2),figsize=(10,7),sharex=False,sharey=False)
    plt.tight_layout(); plt.show()
    if species_col:
        for feature in features:
            df.boxplot(column=feature,by=species_col,figsize=(7,4)); plt.title(feature+" by species"); plt.suptitle(""); plt.show()

def random_array_plots(seed=42):
    rng=np.random.default_rng(seed); values=rng.integers(1,101,50); x=np.arange(1,51)
    fig,axs=plt.subplots(2,2,figsize=(12,8))
    axs[0,0].plot(x,values,marker="o"); axs[0,0].set_title("Line chart")
    axs[0,1].scatter(x,values); axs[0,1].set_title("Scatter plot")
    axs[1,0].hist(values,bins=10,edgecolor="black"); axs[1,0].set_title("Histogram")
    axs[1,1].boxplot(values); axs[1,1].set_title("Box plot")
    for ax in axs.flat: ax.set_xlabel("Observation"); ax.set_ylabel("Value")
    plt.tight_layout(); plt.show(); return values

def dataset_shape_details(path):
    df=pd.read_csv(path)
    print("Shape (rows, columns):",df.shape)
    print("Rows:",len(df),"Columns:",len(df.columns))
    print("Data types:\n",df.dtypes)
    print("Feature names:",df.columns.tolist())
    print("Description:\n",df.describe(include="all"))
    return df

def one_hot_country_label_purchased(path="Data.csv"):
    df=pd.read_csv(path)
    if "Country" not in df or "Purchased" not in df:
        raise ValueError("Expected Country and Purchased columns (check exact column names).")
    df=pd.get_dummies(df,columns=["Country"],dtype=int)
    df["Purchased_encoded"]=LabelEncoder().fit_transform(df["Purchased"].astype(str))
    return df

def standardize_numeric_dataset(path="winequality-red.csv"):
    df=pd.read_csv(path,sep=";" if path.endswith("winequality-red.csv") else ",")
    numeric=df.select_dtypes(include=np.number).columns
    scaler=StandardScaler()
    df.loc[:,numeric]=scaler.fit_transform(df[numeric])
    return df,scaler

def column_mean_median(path):
    df=pd.read_csv(path)
    numeric=df.select_dtypes(include=np.number)
    return pd.DataFrame({"mean":numeric.mean(),"median":numeric.median()})

def manhattan_distance_sum(x,y):
    if len(x)!=len(y): raise ValueError("x and y must have equal lengths")
    return sum(abs(x[i]-x[j])+abs(y[i]-y[j]) for i in range(len(x)) for j in range(i+1,len(x)))

def dataframe_missing_duplicates():
    df=pd.DataFrame({
        "Name":["Asha","Ravi","Meera","Asha","Kabir","Tara","Ravi","Dev",None,"Nina"],
        "Salary":[50000,60000,np.nan,50000,72000,68000,60000,80000,45000,np.nan],
        "Department":["Analytics","IT","HR","Analytics","Finance","IT","IT","Analytics","HR",""]
    })
    print("Original:\n",df)
    cleaned=df.replace(r"^\s*$",np.nan,regex=True).dropna().drop_duplicates()
    print("Cleaned:\n",cleaned)
    return cleaned

def weighted_average_examples():
    arr=np.array([[1,2],[3,4]],dtype=float)
    # Weighted average across columns (axis=0), using one weight per row.
    return np.average(arr,axis=0,weights=[1,3])

def subjects_charts():
    subjects=["Python","SQL","Statistics","Excel","Power BI"]
    marks=[88,82,79,91,85]
    fig,ax=plt.subplots(1,2,figsize=(12,5))
    ax[0].pie(marks,labels=subjects,autopct="%1.1f%%",startangle=90); ax[0].set_title("Marks distribution")
    ax[1].bar(subjects,marks); ax[1].set_ylabel("Marks"); ax[1].set_title("Marks by subject")
    plt.tight_layout(); plt.show()

def student_averages():
    df=pd.DataFrame({"Name":["Hitesh","Imran Qureshi","Faizan"],"Grad_Per":[50,100,50],"Age":[19,30,31]})
    print(df)
    print("Average age:",df["Age"].mean())
    print("Average graduation percentage:",df["Grad_Per"].mean())
    return df

def iris_petal_relationship(path="iris.csv"):
    df=pd.read_csv(path)
    x=next(c for c in ["PetalLengthCm","petal_length"] if c in df.columns)
    y=next(c for c in ["PetalWidthCm","petal_width"] if c in df.columns)
    sp=next((c for c in ["Species","species"] if c in df.columns),None)
    if sp:
        for species,grp in df.groupby(sp): plt.scatter(grp[x],grp[y],label=species)
        plt.legend()
    else: plt.scatter(df[x],df[y])
    plt.xlabel("Petal length"); plt.ylabel("Petal width"); plt.title("Petal length vs width"); plt.show()

def flattened_array_min_max():
    a=np.arange(4).reshape(2,2)
    return np.max(a),np.min(a)

if __name__=="__main__":
    print("Example Manhattan distance sum:",manhattan_distance_sum([-1,1,3,2],[5,6,5,3]))
    print("Example weighted average:",weighted_average_examples())
    student_averages()
