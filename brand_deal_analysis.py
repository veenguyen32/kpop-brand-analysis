import pandas as pd
import matplotlib.pyplot as plt

# Load & clean data
file_path = "Korean Idols Ambassadorials - BRAND DEALS.csv"
df = pd.read_csv(file_path, encoding='latin1')

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Drop rows with missing key values
df = df.dropna(subset=['Name', 'Gender', 'Solo/Group', 'Main Brand', 'Company'])

#Gender vs Solo/Group
grouped_gender_solo = df.groupby(['Gender', 'Solo/Group']).size().unstack(fill_value=0)
print("🔎 Gender vs Solo/Group :\n", grouped_gender_solo)

# Plot Gender vs Solo/Group
plt.figure(figsize=(8, 5))
grouped_gender_solo.plot(kind='bar', stacked=True, color=['#FFB6C1', '#87CEFA'])
plt.title("Brand Deals by Gender and Solo/Group")
plt.xlabel("Gender")
plt.ylabel("Number of Deals")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("gender_solo_group.png")
plt.show()

# Gender vs Company
grouped_company_gender = df.groupby(['Company', 'Gender']).size().unstack(fill_value=0)
grouped_company_gender['Total'] = grouped_company_gender.sum(axis=1)
grouped_company_gender = grouped_company_gender.sort_values('Total', ascending=False).drop(columns='Total')

print("\nGender vs Company:\n", grouped_company_gender)

# Plot Company vs Gender
plt.figure(figsize=(10, 6))
grouped_company_gender.plot(kind='barh', stacked=True, color=['#FFB6C1', '#87CEFA'])
plt.title("Brand Deals by Company and Gender")
plt.xlabel("Number of Deals")
plt.ylabel("Company")
plt.tight_layout()
plt.savefig("company_gender.png")
plt.show()

# Gender vs Brand
grouped_brand_gender = df.groupby(['Main Brand', 'Gender']).size().unstack(fill_value=0)
grouped_brand_gender['Total'] = grouped_brand_gender.sum(axis=1)
grouped_brand_gender = grouped_brand_gender.sort_values('Total', ascending=False).drop(columns='Total')

print("\n Gender vs Brand :\n", grouped_brand_gender.head(10))

# Plot Top 10 Brands by Gender
top_10_brands = grouped_brand_gender.head(10)
top_10_brands.plot(kind='bar', figsize=(10, 6), color=['#FFB6C1', '#87CEFA'])
plt.title("Top 10 Brands by Gender")
plt.xlabel("Brand")
plt.ylabel("Number of Deals")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_brands_gender.png")
plt.show()

# Save grouped summaries to CSV
grouped_gender_solo.to_csv("summary_gender_solo_group.csv")
grouped_company_gender.to_csv("summary_company_gender.csv")
grouped_brand_gender.to_csv("summary_brand_gender.csv")

Add main analysis script
