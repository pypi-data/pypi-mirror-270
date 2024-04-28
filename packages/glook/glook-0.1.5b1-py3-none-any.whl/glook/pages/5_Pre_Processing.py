# page2.py
import streamlit as st
st.set_page_config(
		page_title="ML-Automation", 
		page_icon="🏗️", 
		layout="wide", 
		initial_sidebar_state = "expanded")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import statsmodels.api as sm
st.set_option('deprecation.showPyplotGlobalUse', False)
# from wordcloud import WordCloud
from scipy.stats.mstats import winsorize
from sklearn.impute import SimpleImputer
from scipy.stats import boxcox, yeojohnson
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, KBinsDiscretizer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg')
# st.title("1️⃣Univariate Analysis")
Confirm_Change = False
def limit_unique_values(series, limit=20):
	if series.nunique() > limit:
		top_categories = series.value_counts().index[:limit]
		return series.apply(lambda x: x if x in top_categories else 'Other')
	else:
		return series

def limit_unique_values_cloud(series, limit=200):
	if series.nunique() > limit:
		top_categories = series.value_counts().index[:limit]
		return top_categories
	else:
		return series.unique()

# def limit_unique_values_cloud(series, limit=200):
# 	if series.nunique() > limit:
# 		top_categories = series.value_counts().index[:limit]
# 		return series.apply(lambda x: x if x in top_categories else 'Other')
# 	else:
# 		return series
def change_dtype(df, column_name, new_dtype):
	try:
		df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
		df[column_name] = df[column_name].astype(new_dtype)
		# st.success(f"Successfully changed data type of column '{column_name}' to {new_dtype}.")
		st.warning(f"Data type of column '{column_name}' changed to {new_dtype}, but these changes won't be saved until you press the 'Confirm Changes' button below.")
	except Exception as e:
		st.warning("Select Proper Column")
		st.error(f"Error occurred: {e}")

# Function to preprocess column by dropping it
def drop_column(df, column_name):
	try:
		df.drop(column_name, axis=1, inplace=True)
		st.warning(
			f"Column '{column_name}' has been dropped, but changes won't be saved until you press the 'Confirm Changes' button below."
		)
	except Exception as e:
		st.error(f"Error occurred: {e}")

# Function to preprocess by dropping duplicates
def drop_duplicates(df):
	try:
		original_rows = len(df)
		df.drop_duplicates(inplace=True)
		new_rows = len(df)
		st.warning(f"Dropped {original_rows - new_rows} duplicate rows, but changes will not be saved until you press the 'Confirm Changes' button below.")
	except Exception as e:
		st.error(f"Error occurred: {e}")


# Function to preprocess by treating outliers
def treat_outliers(df, column_name, method):
	try:
		if method == "Delete Outliers":
			# Define your outlier detection and deletion method here
			# For example, you can use z-score method to detect and delete outliers
			z_scores = np.abs((df[column_name] - df[column_name].mean()) / df[column_name].std())
			df = df[z_scores < 3]  # Remove rows with z-scores greater than 3
			
			# st.success("Outliers deleted successfully.")
			st.warning("Outliers deleted. Changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Winsorization":
			print(0)
			# df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
			# df = df.reset_index()
			# ser = pd.Series([2, pd.NA], dtype=pd.Int64Dtype())
			# df[column_name] = pd.Series(df[column_name], dtype=pd.Int64Dtype)
			# df[column_name] = df[column_name].astype(pd.Int64Dtype())
			# Slider for selecting the lower limit for Winsorization
			print(2)
			lower_limit = st.slider("Select Lower Limit", min_value=0.0, max_value=0.1, step=0.01, value=0.05)
			# Slider for selecting the upper limit for Winsorization
			upper_limit = st.slider("Select Upper Limit", min_value=0.0, max_value=0.1, step=0.01, value=0.05)

			# Apply Winsorization to the column
			modified_column = winsorize(df[column_name], limits=[lower_limit, upper_limit])
			print(3)
			df[column_name] = modified_column
			
			st.warning("Outliers have been treated using Winsorization, but changes will not be saved until the 'Confirm Changes' button is pressed.")
			return df
	except Exception as e:
		print(e)
		# st.error(f"Error occurred: {e}")
		# st.error("🚨 Select Proper Numerical Column")
		st.warning("Select Proper Numerical Column")
		return df
	
# Function to preprocess by treating outliers
def treat_outliers_full_df(df, method, z_score_threshold=3, lower_limit=0.05, upper_limit=0.05):
	"""
	Treat outliers in a given DataFrame.

	:param df: DataFrame to process
	:param method: Method to use for outlier treatment ("Delete Outliers", "Winsorization")
	:param z_score_threshold: Z-score threshold for identifying outliers (used for "Delete Outliers")
	:param lower_limit: Lower limit for Winsorization
	:param upper_limit: Upper limit for Winsorization
	:return: DataFrame with outliers treated
	"""
	try:
		# Get a list of all numerical columns
		numerical_columns = df.select_dtypes(include=[np.number]).columns.tolist()

		if method == "Delete Outliers":
			# Remove rows with z-scores greater than the specified threshold for each numerical column
			for column_name in numerical_columns:
				z_scores = np.abs((df[column_name] - df[column_name].mean()) / df[column_name].std())
				df = df[z_scores < z_score_threshold]  # Retain rows with z-scores less than the threshold
			# st.success("Outliers deleted successfully.")
			st.warning("Outliers deleted. Changes will not be saved until you press the 'Confirm Changes' button below.")
			return df

		elif method == "Winsorization":
			# Apply Winsorization to each numerical column with the specified limits
			for column_name in numerical_columns:
				df[column_name] = winsorize(df[column_name], limits=[lower_limit, upper_limit])
			# st.success("Outliers treated using Winsorization successfully.")
			st.warning("Outliers have been treated using Winsorization, but changes will not be saved until the 'Confirm Changes' button is pressed.")
			return df

		else:
			st.error("Invalid method specified for treating outliers.")
			return df

	except Exception as e:
		st.warning(f"Error occurred: {e}")
		return df

# Function to preprocess by treating missing values
def treat_missing_values(df, column_name, method):
	try:
		if method == "Delete Missing Values":
			df.dropna(subset=[column_name], inplace=True)
			# st.success("Missing values deleted successfully.")
			st.warning("Missing values have been deleted, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Mean Imputation":
			imputer = SimpleImputer(strategy="mean")
			df[column_name] = imputer.fit_transform(df[[column_name]])
			# st.success("Missing values imputed using mean successfully.")
			st.warning("Missing values have been imputed using the mean, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Median Imputation":
			imputer = SimpleImputer(strategy="median")
			df[column_name] = imputer.fit_transform(df[[column_name]])
			# st.success("Missing values imputed using median successfully.")
			st.warning("Missing values have been imputed using the median, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Mode Imputation":
			imputer = SimpleImputer(strategy="most_frequent")
			df[column_name] = imputer.fit_transform(df[[column_name]])
			# st.success("Missing values imputed using mode successfully.")
			st.warning("Missing values have been imputed using the mode, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
	except Exception as e:
		st.error(f"Error occurred: {e}")
		return df

# Function to preprocess by applying transformation techniques
def apply_transformation(df, column_name, method):
	try:
		if method == "Log Transformation":
			df[column_name] = np.log1p(df[column_name])
			# st.success("Log transformation applied successfully.")
			st.warning("Log transformation applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Exponential Transformation":
			df[column_name] = np.exp(df[column_name])
			# st.success("Exponential transformation applied successfully.")
			st.warning("Exponential transformation applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Square Root Transformation":
			df[column_name] = np.sqrt(df[column_name])
			# st.success("Square root transformation applied successfully.")
			st.warning("Square root transformation applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Box-Cox Transformation":
			transformed_data, _ = boxcox(df[column_name] + 1)  # Adding 1 to avoid non-positive values
			df[column_name] = transformed_data
			# st.success("Box-Cox transformation applied successfully.")
			st.warning("Box-Cox transformation applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Yeo-Johnson Transformation":
			transformed_data, _ = yeojohnson(df[column_name] + 1)  # Adding 1 to avoid non-positive values
			df[column_name] = transformed_data
			# st.success("Yeo-Johnson transformation applied successfully.")
			st.warning("Yeo-Johnson transformation applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
	except Exception as e:
		st.warning("Select Proper Column")
		st.error(f"Error occurred: {e}")
		return df


# Function to preprocess by creating dummy variables
def create_dummy_variables(df, method):
	try:
		if method == "One-Hot Encoding":
			# Perform one-hot encoding for all categorical columns
			opt = st.toggle("drop_first")
			cat_columns = df.select_dtypes(include=['object']).columns
			encoded_df = pd.get_dummies(df, columns=cat_columns, drop_first=opt)
			encoded_df.replace({True: 1, False: 0}, inplace=True)
			# st.success("One-hot encoding applied successfully.")
			st.warning("One-hot encoding applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return encoded_df
		elif method == "Label Encoding":
			# Perform label encoding for all categorical columns
			encoded_df = df.copy()
			label_encoder = LabelEncoder()
			for column in encoded_df.select_dtypes(include=['object']).columns:
				encoded_df[column] = label_encoder.fit_transform(encoded_df[column])
			# st.success("Label encoding applied successfully.")
			st.warning("Label encoding applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return encoded_df
	except Exception as e:
		st.error(f"Error occurred: {e}")
		return df


# Function to preprocess by creating dummy variables
def create_dummy_variables_for_col(df, column_name, method):
	try:
		if method == "One-Hot Encoding":
			# Perform one-hot encoding
			encoded_df = pd.get_dummies(df[column_name], prefix=column_name)
			df = pd.concat([df, encoded_df], axis=1)
			df.drop(column_name, axis=1, inplace=True)
			df.replace({True: 1, False: 0}, inplace=True)
			# st.success("One-hot encoding applied successfully.")
			st.warning("One-hot encoding applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
		elif method == "Label Encoding":
			# Perform label encoding
			label_encoder = LabelEncoder()
			df[column_name] = label_encoder.fit_transform(df[column_name])
			# st.success("Label encoding applied successfully.")
			st.warning("Label encoding applied, but changes will not be saved until you press the 'Confirm Changes' button below.")
			return df
	except Exception as e:
		st.error(f"Error occurred: {e}")
		return df


# Function to preprocess by applying scaling
def apply_scaling(df, method):
	try:
		if method == "Standardize Scaling":
			scaler = StandardScaler()
			scaled_data = scaler.fit_transform(df)
			scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
			# st.success("Robust scaling applied successfully.")
			st.warning("Standardize scaling has been applied, but the changes will not be saved until you press the 'Confirm Changes' button below.")
			return scaled_df
		elif method == "Min-Max Scaling":
			scaler = MinMaxScaler()
			scaled_data = scaler.fit_transform(df)
			scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
			# st.success("Robust scaling applied successfully.")
			st.warning("Min-Max scaling has been applied, but the changes will not be saved until you press the 'Confirm Changes' button below.")
			return scaled_df
		elif method == "Robust Scaling":
			scaler = RobustScaler()
			scaled_data = scaler.fit_transform(df)
			scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
			# st.success("Robust scaling applied successfully.")
			st.warning("Robust scaling has been applied, but the changes will not be saved until you press the 'Confirm Changes' button below.")
			return scaled_df
	except Exception as e:
		st.warning("Only Numerical Columns Should be present.")
		st.error(f"Error occurred: {e}")
		return df


# Function to discretize output variable
# Function to discretize output variable
def discretize_output(df, column_name, bins, strategy):
	try:
		discretizer = KBinsDiscretizer(n_bins=bins, encode='ordinal', strategy=strategy)
		df[column_name] = discretizer.fit_transform(df[[column_name]])
		# st.success(f"Output variable '{column_name}' discretized successfully.")
		st.warning(f"Output variable '{column_name}' discretized, but changes will not be saved until you press the 'Confirm Changes' button below.")
		return df
	except Exception as e:
		st.warning("Works for only numerical columns")
		st.error(f"Error occurred: {e}")
		return df

def calculate_insights(column_data):
	try:
		insights = {}

		# Count of distinct values
		insights['Distinct'] = len(column_data.dropna().unique())

		# Percentage of distinct values
		insights['Distinct (%)'] = len(column_data.dropna().unique()) / len(column_data.dropna()) * 100

		# Count of missing values
		insights['Missing'] = column_data.isnull().sum()

		# Percentage of missing values
		insights['Missing (%)'] = column_data.isnull().sum() / len(column_data) * 100

		# Count of infinite values
		insights['Infinite'] = np.isinf(column_data).sum()

		# Percentage of infinite values
		insights['Infinite (%)'] = np.isinf(column_data).sum() / len(column_data) * 100

		# Mean
		insights['Mean'] = column_data.mean()

		# Median
		insights['Median'] = column_data.median()

		# Mode
		insights['Mode'] = column_data.mode().iloc[0]

		# Minimum
		insights['Minimum'] = column_data.min()

		# Maximum
		insights['Maximum'] = column_data.max()

		# Zeros count
		insights['Zeros'] = (column_data == 0).sum()

		# Percentage of zeros
		insights['Zeros (%)'] = (column_data == 0).sum() / len(column_data) * 100

		# Negative values count
		insights['Negative'] = (column_data < 0).sum()

		# Percentage of negative values
		insights['Negative (%)'] = (column_data < 0).sum() / len(column_data) * 100

		# Memory size
		insights['Memory size'] = column_data.memory_usage(deep=True)

		# 5th percentile
		insights['5-th percentile'] = np.percentile(column_data.dropna(), 5)

		# Q1 (25th percentile)
		insights['Q1'] = np.percentile(column_data.dropna(), 25)

		# Median
		insights['Median'] = np.median(column_data.dropna())

		# Q3 (75th percentile)
		insights['Q3'] = np.percentile(column_data.dropna(), 75)

		# 95th percentile
		insights['95-th percentile'] = np.percentile(column_data.dropna(), 95)

		# Range
		insights['Range'] = insights['Maximum'] - insights['Minimum']

		# Interquartile range (IQR)
		insights['Interquartile range'] = insights['Q3'] - insights['Q1']

		# Descriptive statistics
		insights['Descriptive statistics'] = column_data.describe()

		# Standard deviation
		insights['Standard deviation'] = column_data.std()

		# Coefficient of variation (CV)
		if insights['Mean'] != 0:
			insights['Coefficient of variation (CV)'] = insights['Standard deviation'] / insights['Mean']
		else:
			insights['Coefficient of variation (CV)'] = float('NaN')

		# Kurtosis
		insights['Kurtosis'] = column_data.kurtosis()

		# Median Absolute Deviation (MAD)
		mad = np.median(np.abs(column_data.dropna() - np.median(column_data.dropna())))
		insights['Median Absolute Deviation (MAD)'] = mad

		# Skewness
		insights['Skewness'] = column_data.skew()

		# Sum
		insights['Sum'] = column_data.sum()

		# Variance
		insights['Variance'] = column_data.var()

		# Monotonicity (not calculated)
	except Exception as e:
		print("_e:=_", e)
		st.write(e)
		

	return insights



# Initialize state
if "button_clicked" not in st.session_state:
	st.session_state.button_clicked = False
def callback():
	# Button was clicked!
	st.session_state.button_clicked = True


st.subheader(":green[Try Best Pre-Processing Step]")
try:
	st.write("Session State:->", st.session_state["shared"])
	if "df" in st.session_state:
		df = st.session_state.df
		print(1)
		# int_columns = df.select_dtypes(include='int').columns
		# df[int_columns] = df[int_columns].astype(pd.Int64Dtype())
		selected_column = st.selectbox("Select a column", df.columns)
		print(2)
		st.subheader(f"Insights for column ':green[{selected_column}]':")
		print(3)
		if df[selected_column].dtype == 'object':
			col1, col2 = st.columns(2)
			print(4)
			with col1:
				unique_values = df[selected_column].nunique()
				print(5)
				st.write(f"  - Data Type: :green[{df[selected_column].dtype}]")
				print(6)
				st.write(f"  - Number of Unique Values: :green[{unique_values}]")
				print(7)
				if unique_values <= 20:
					print(8)
					st.write(f"  - Unique Values: :green[{', '.join(map(str, df[selected_column].unique()))}]")
				else:
					print(9)
					st.write(f"  - Top 20 Unique Values:")
					print(10)
					st.write(f":green[{', '.join(map(str, df[selected_column].value_counts().head(20).index))}]")
			with col2:
				print(10)
				plt.figure(figsize=(10, 6))
				print(11)
				try:
					print(12)
					sns.countplot(x=limit_unique_values(df[selected_column]), data=df, color="green")
				except:
					print(13)
					sns.countplot(x=df[selected_column], data=df, color="green")
				plt.xticks(rotation=45)
				st.pyplot()
				plt.close()
			with st.expander("More Info"):
				print(14)
				tab1, tab2 = st.tabs(["Insights", "Donut chart"])
				print(15)
				with tab1:
					print(16)
					col7, col8, col9 = st.columns(3)
					with col7:
						print(17)
						# Insights
						st.write("## Insights")
						approximate_distinct_count = df[selected_column].nunique()
						approximate_unique_percent = (approximate_distinct_count / len(df)) * 100
						missing = df[selected_column].isna().sum()
						missing_percent = (missing / len(df)) * 100
						memory_size = df[selected_column].memory_usage(deep=True)
						st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
						st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
						st.write(f"Missing: :green[{missing}]")
						st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
						st.write(f"Memory Size: :green[{memory_size}]")
						print(18)
						# st.header("An owl")
						# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
					with col8:
						print(19)
						# Mode and Standard Deviation
						st.write("## Mode")
						# if df[selected_column].dtype == 'object':
						mode = df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
						st.write(f"Mode: :green[{mode}]")
							# st.write("Standard Deviation cannot be calculated for non-numeric data.")
						# else:
							# mode = df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
							# std_dev = df[selected_column].astype(float).std()
							# st.write(f"Mode: {mode}")
							# st.write(f"Standard Deviation: {std_dev}")
						print(20)
					with col9:
						print(21)
						# First 5 Sample Rows
						st.write("## First 5 Sample Rows")
						st.write(df[selected_column].head())
						print(22)
				with tab2:
					print(23)
					# Prepare data for donut chart
					data = limit_unique_values(df[selected_column]).value_counts().reset_index()
					data.columns = [selected_column, 'count']

					fig = px.pie(data, values='count', names=selected_column, hole=0.5)
					fig.update_traces(textposition='inside', textinfo='percent+label')
					fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
					st.plotly_chart(fig)
					print(24)
					# st.header("An owl")
					# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

				
		elif pd.api.types.is_numeric_dtype(df[selected_column]):
			print(25)
			col3, col4 = st.columns(2)
			print(26)
			with col3:
				print(27)
				st.write(f"  - Data Type: :green[{df[selected_column].dtype}]")
				st.write(f"  - Mean: :green[{df[selected_column].mean()}]")
				st.write(f"  - Standard Deviation: :green[{df[selected_column].std()}]")
				st.write(f"  - Min Value: :green[{df[selected_column].min()}]")
				st.write(f"  - Max Value: :green[{df[selected_column].max()}]")
				print(28)
			with col4:
				plt.figure(figsize=(10, 6))
				sns.histplot(df[selected_column], kde=True, color="green")
				st.pyplot()
				plt.close()
				print(29)
			with st.expander("More Info"):
				print(30)
				tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
				with tab1:
					print(31)
					col4, col5, col6 = st.columns(3)
					with col4:
						print(32)
						st.write("#### Basic Statistics")
						insights = calculate_insights(df[selected_column])
						basic_stats = {key: value for key, value in insights.items() if key in [
							'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
						for key, value in basic_stats.items():
							st.write(f"**{key}:** :green[{value:.3f}]")
						st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
						st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
						st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")
						print(33)
					with col5:
						print(34)
						st.write("#### Percentiles")
						descriptive_stats = insights.get('Descriptive statistics')
						if descriptive_stats is not None:
							percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
							if '5%' in descriptive_stats.index:
								percentiles['5%'] = descriptive_stats['5%']
							if '95%' in descriptive_stats.index:
								percentiles['95%'] = descriptive_stats['95%']
							st.write(percentiles)
						print(35)

					with col6:
						print(36)
						st.write("#### Additional Statistics")
						additional_stats = {key: value for key, value in insights.items() if key in [
							'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
						for key, value in additional_stats.items():
							st.write(f"**{key}:** :green[{value:.3f}]")
						# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
						# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
						# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
						st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
						st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
						st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						print(37)
				with tab2:
					print(38)
					fig = px.box(df, y=selected_column)
					st.plotly_chart(fig)
					print(39)
				with tab3:
					print(40)
					plt.figure(figsize=(10, 6))
					qqplot_data = sm.qqplot(df[selected_column], line='s').gca().lines
					fig = go.Figure()
					fig.add_trace({
						'type': 'scatter',
						'x': qqplot_data[0].get_xdata(),
						'y': qqplot_data[0].get_ydata(),
						'mode': 'markers',
						'marker': {'color': '#19d3f3'}
					})
					fig.add_trace({
						'type': 'scatter',
						'x': qqplot_data[1].get_xdata(),
						'y': qqplot_data[1].get_ydata(),
						'mode': 'lines',
						'line': {'color': '#636efa'}
					})
					x_min = min(qqplot_data[0].get_xdata())
					x_max = max(qqplot_data[0].get_xdata())
					y_min = min(qqplot_data[0].get_ydata())
					y_max = max(qqplot_data[0].get_ydata())
					fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
					fig.update_layout({
						'title': f'QQ Plot for {selected_column}',
						'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
						'yaxis': {'title': 'Sample Quantiles'},
						'showlegend': False,
						'width': 800,
						'height': 700,
					})
					st.plotly_chart(fig)
					print(41)
		# st.write("---")
	else:
		st.write("DataFrame not found.")
	# st.write("``")
except ZeroDivisionError:
	pass
except Exception as e:
	st.error(e)
	st.subheader("⚠️Please upload a file⚠️")
	pass

# Function to preprocess column by changing data type



# Select column to preprocess
# selected_column = st.selectbox("Select a column", df.columns)
		
print(42)

# Select preprocessing action
preprocessing_action = st.sidebar.radio("Select preprocessing action", 
									[
										"Select Pre-Processing Step⬇️",
										"Change Data Type", 
										"Drop Column", 
										"Drop Duplicates", 
										"Treat Outliers", 
										"Treat Outliers on full DF",
										"Treat Missing Values",
										"Traat Missing from full DF",
										"Apply Transformation",
										"Create Dummy Variables",
										"Column to Dummy Variable",
										"Apply Scaling",
										"Discretize Output Variable",
										"Column Unique Value Replacement"
									]
									)

# modified_df = pd.DataFrame()
try:
	if preprocessing_action == "Select Pre-Processing Step⬇️":
		print("You have successfuly reached Pre-Proceaaing Phase")

	elif preprocessing_action == "Change Data Type":
		dtype_options = [
			"int", "int32", "Int32", "int64", "Int64",
			"float", "float32", "Float32", "float64", "Float64",
			"str", "bool"
		]
		new_dtype = st.selectbox("Select new data type", dtype_options)
		# Apply = st.button('Apply')
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
		# if Apply:
			# Make a copy of the original DataFrame to preserve undo functionality
			modified_df = df.copy()
			
			change_dtype(modified_df, selected_column, new_dtype)
			st.write("Modified DataFrame:")
			st.write(modified_df)
			# st.session_state.df = modified_df  # Store modified DataFrame in session state
			# st.session_state.modified_df = modified_df
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				st.error(e)
				st.subheader("⚠️Please upload a file⚠️")
				pass

			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()


	elif preprocessing_action == "Drop Column":
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
		# if Apply:
			# Make a copy of the original DataFrame to preserve undo functionality
			modified_df = df.copy()
			
			drop_column(modified_df, selected_column)
			st.write("Modified DataFrame:")
			st.write(modified_df)
			# st.session_state.df = modified_df  # Store modified DataFrame in session state
			# st.session_state.modified_df = modified_df
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				# st.error(e)
				# st.subheader("⚠️Please upload a file⚠️")
				pass

			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()


	elif preprocessing_action == "Drop Duplicates":
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			
			drop_duplicates(modified_df)
			st.write("Modified DataFrame:")
			st.write(modified_df)

			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()


	elif preprocessing_action == "Treat Outliers":
		outlier_method = st.radio("Select Outlier Treatment Method", ["Delete Outliers", "Winsorization"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			
			modified_df = treat_outliers(modified_df, selected_column, outlier_method)
			st.write("Modified DataFrame:")
			st.write(modified_df)
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				st.error(e)
				st.subheader("⚠️Please upload a file⚠️")
				pass

			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()



	elif preprocessing_action == "Treat Outliers on full DF":
		# outlier_method = st.radio("Select Outlier Treatment Method", ["Delete Outliers", "Winsorization"])
		method = st.selectbox("Select Method to Treat Outliers", ["Delete Outliers", "Winsorization"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			# Z-score threshold input for "Delete Outliers"
			if method == "Delete Outliers":
				z_score_threshold = st.slider(
					"Select Z-Score Threshold",
					min_value=1.0,
					max_value=5.0,
					step=0.1,
					value=3.0,
				)
			else:
				z_score_threshold = 3.0  # Default value if not used
			if method == "Winsorization":

				# method = st.selectbox("Select Method to Treat Outliers", ["Delete Outliers", "Winsorization"])
				lower_limit = st.slider("Select Lower Limit:", min_value=0.0, max_value=0.1, step=0.01, value=0.05)
				# Slider for selecting the upper limit for Winsorization
				upper_limit = st.slider("Select Upper Limit:", min_value=0.0, max_value=0.1, step=0.01, value=0.05)
			else:
				lower_limit = upper_limit = 0.05
			modified_df = treat_outliers_full_df(modified_df, method, z_score_threshold=3, lower_limit=lower_limit, upper_limit=upper_limit)
			st.write("Modified DataFrame:")
			st.write(modified_df)

			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()





	elif preprocessing_action == "Treat Missing Values":
		missing_method = st.radio("Select Missing Value Treatment Method", ["Delete Missing Values", "Mean Imputation", "Median Imputation", "Mode Imputation"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			modified_df = treat_missing_values(modified_df, selected_column, missing_method)
			st.write("Modified DataFrame:")
			st.write(modified_df)
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				st.error(e)
				st.subheader("⚠️Please upload a file⚠️")
				pass

			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()


	elif preprocessing_action == "Traat Missing from full DF":
		st.write("hi")
		# Determine numeric and categorical columns
		numeric_columns = df.select_dtypes(include=np.number).columns
		categorical_columns = df.select_dtypes(include=['object', 'category']).columns
		
		# Ask user for treatment options for numeric columns
		numeric_treatment = st.selectbox("Select treatment for missing values in numeric columns", ["Mean", "Median", "Mode", "Random"])
		numeric_strategy = None
		if numeric_treatment == "Random":
			numeric_strategy = st.text_input("Enter strategy for random value generation (e.g., 'uniform', 'normal')")

		# Ask user for treatment options for categorical columns
		categorical_treatment = st.selectbox("Select treatment for missing values in categorical columns", ["Mode", "Random"])
		categorical_strategy = None
		if categorical_treatment == "Random":
			categorical_strategy = st.text_input("Enter strategy for random value generation (e.g., 'uniform', 'normal')")
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			# Apply treatment for numeric columns
			for column in numeric_columns:
				if numeric_treatment == "Mean":
					modified_df[column].fillna(modified_df[column].mean(), inplace=True)
				elif numeric_treatment == "Median":
					modified_df[column].fillna(modified_df[column].median(), inplace=True)
				elif numeric_treatment == "Mode":
					modified_df[column].fillna(modified_df[column].mode()[0], inplace=True)
				elif numeric_treatment == "Random":
					modified_df[column].fillna(np.random.RandomState().choice(modified_df[column].dropna()), inplace=True)
			# Apply treatment for categorical columns
			for column in categorical_columns:
				if categorical_treatment == "Mode":
					modified_df[column].fillna(modified_df[column].mode()[0], inplace=True)
				elif categorical_treatment == "Random":
					modified_df[column].fillna(np.random.RandomState().choice(modified_df[column].dropna()), inplace=True)

			st.write("Modified DataFrame:")
			st.write(modified_df)
			confirm_change = st.button('Confirm Change')

			if confirm_change:
				modified_df.to_csv('data.csv', index=False)
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()


	elif preprocessing_action == "Apply Transformation":
		transformation_method = st.selectbox("Select Transformation Technique", ["Log Transformation", "Exponential Transformation", "Square Root Transformation", "Box-Cox Transformation", "Yeo-Johnson Transformation"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			modified_df = apply_transformation(modified_df, selected_column, transformation_method)
			st.write("Modified DataFrame:")
			st.write(modified_df)
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				st.error(e)
				st.subheader("⚠️Please upload a file⚠️")
				pass

	# col11, col22 = st.columns(2)
	# with col11:
			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()

	elif preprocessing_action == "Create Dummy Variables":
		encoding_method = st.selectbox("Select encoding method", ["One-Hot Encoding", "Label Encoding"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			modified_df = create_dummy_variables(modified_df, encoding_method)
			st.write("Modified DataFrame:")
			st.write(modified_df)
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				# st.error(e)
				# st.subheader("⚠️Please upload a file⚠️")
				pass

	# col11, col22 = st.columns(2)
	# with col11:
			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()


	elif preprocessing_action == "Column to Dummy Variable":
		encoding_method = st.selectbox("Select encoding method", ["One-Hot Encoding", "Label Encoding"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			modified_df = create_dummy_variables_for_col(modified_df, selected_column, encoding_method)
			st.write("Modified DataFrame:")
			st.write(modified_df)
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				# st.error(e)
				# st.subheader("⚠️Please upload a file⚠️")
				pass

	# col11, col22 = st.columns(2)
	# with col11:
			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()


	elif preprocessing_action == "Apply Scaling":
		scaling_method = st.selectbox("Select scaling method", ["Standardize Scaling", "Min-Max Scaling", "Robust Scaling"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			modified_df = apply_scaling(modified_df, scaling_method)
			st.write("Modified DataFrame:")
			st.write(modified_df)

	# col11, col22 = st.columns(2)
	# with col11:
			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				# modified_df.to_csv('data4.csv', index=False)
				st.rerun()



	elif preprocessing_action == "Discretize Output Variable":
		# output_column = st.selectbox("Select output variable", df.columns)
		bins = st.slider("Select the number of bins", min_value=2, max_value=20, value=5)
		strategy = st.selectbox("Select the strategy for binning", ["uniform", "quantile", "kmeans"])
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			modified_df = df.copy()
			modified_df = discretize_output(modified_df, selected_column, bins, strategy)		
			st.write("Modified DataFrame:")
			st.write(modified_df)
			try:
				if modified_df[selected_column].dtype == 'object':
					col1, col2 = st.columns(2)
					with col1:
						unique_values = modified_df[selected_column].nunique()
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						if unique_values <= 20:
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
						else:
							st.write(f"  - Top 20 Unique Values:")
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
					with col2:
						plt.figure(figsize=(10, 6))
						try:
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2 = st.tabs(["Insights", "Donut chart"])
						with tab1:
							col7, col8, col9 = st.columns(3)
							with col7:
								# Insights
								st.write("## Insights")
								approximate_distinct_count = modified_df[selected_column].nunique()
								approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
								missing = modified_df[selected_column].isna().sum()
								missing_percent = (missing / len(modified_df)) * 100
								memory_size = modified_df[selected_column].memory_usage(deep=True)
								st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
								st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
								st.write(f"Missing: :green[{missing}]")
								st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
								st.write(f"Memory Size: :green[{memory_size}]")

								# st.header("An owl")
								# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
							with col8:
								# Mode and Standard Deviation
								st.write("## Mode")
								# if modified_df[selected_column].dtype == 'object':
								mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
								st.write(f"Mode: :green[{mode}]")
									# st.write("Standard Deviation cannot be calculated for non-numeric data.")
								# else:
									# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
									# std_dev = modified_df[selected_column].astype(float).std()
									# st.write(f"Mode: {mode}")
									# st.write(f"Standard Deviation: {std_dev}")
							with col9:
								# First 5 Sample Rows
								st.write("## First 5 Sample Rows")
								st.write(modified_df[selected_column].head())

						with tab2:
							# Prepare data for donut chart
							data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
							data.columns = [selected_column, 'count']

							fig = px.pie(data, values='count', names=selected_column, hole=0.5)
							fig.update_traces(textposition='inside', textinfo='percent+label')
							fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
							st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					col3, col4 = st.columns(2)
					with col3:
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					with st.expander("More Info"):
						tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
						with tab1:
							col4, col5, col6 = st.columns(3)
							with col4:
								st.write("#### Basic Statistics")
								insights = calculate_insights(modified_df[selected_column])
								basic_stats = {key: value for key, value in insights.items() if key in [
									'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
								for key, value in basic_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
								st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
								st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

							with col5:
								st.write("#### Percentiles")
								descriptive_stats = insights.get('Descriptive statistics')
								if descriptive_stats is not None:
									percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
									if '5%' in descriptive_stats.index:
										percentiles['5%'] = descriptive_stats['5%']
									if '95%' in descriptive_stats.index:
										percentiles['95%'] = descriptive_stats['95%']
									st.write(percentiles)

							with col6:
								st.write("#### Additional Statistics")
								additional_stats = {key: value for key, value in insights.items() if key in [
									'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
								for key, value in additional_stats.items():
									st.write(f"**{key}:** :green[{value:.3f}]")
								# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
								# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
								# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
								st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
								st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
								st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
						with tab2:
							fig = px.box(modified_df, y=selected_column)
							st.plotly_chart(fig)
						with tab3:
							plt.figure(figsize=(10, 6))
							qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
							fig = go.Figure()
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[0].get_xdata(),
								'y': qqplot_data[0].get_ydata(),
								'mode': 'markers',
								'marker': {'color': '#19d3f3'}
							})
							fig.add_trace({
								'type': 'scatter',
								'x': qqplot_data[1].get_xdata(),
								'y': qqplot_data[1].get_ydata(),
								'mode': 'lines',
								'line': {'color': '#636efa'}
							})
							x_min = min(qqplot_data[0].get_xdata())
							x_max = max(qqplot_data[0].get_xdata())
							y_min = min(qqplot_data[0].get_ydata())
							y_max = max(qqplot_data[0].get_ydata())
							fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
							fig.update_layout({
								'title': f'QQ Plot for {selected_column}',
								'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
								'yaxis': {'title': 'Sample Quantiles'},
								'showlegend': False,
								'width': 800,
								'height': 700,
							})
							st.plotly_chart(fig)
					st.write("---")
				else:
					st.write("DataFrame not found.")
				st.write("``")
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				pass
			except Exception as e:
				st.error(e)
				st.subheader("⚠️Please upload a file⚠️")
				pass

	# col11, col22 = st.columns(2)
	# with col11:
			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				st.rerun()

	elif preprocessing_action == "Column Unique Value Replacement":
		print(43)
		select = st.selectbox("Convert type:", ["Convert to Str:", "Convert to int:", "Convert to float:"])
		
		# Select a categorical column
		# selected_column = st.selectbox("Select a categorical column", categorical_columns)

		# Get distinct categorical values
		print(44)
		distinct_values = df[selected_column].unique()
		print(45)
		# Display distinct categorical values and input box for replacement
		replacements = {}
		for value in distinct_values:
			print(46)
			if select == "Convert to Str:":
				print(47)
				replacements[value] = st.text_input(f"Replace '{value}' with:", value=str(value))
			elif select == "Convert to int:":
				try:
					print(48)
					replacements[value] = st.number_input(f"Replace '{value}' with:", value=int(value), step=1)
				except:
					print(49)
					replacements[value] = st.number_input(f"Replace '{value}' with:", step=1)
			elif select == "Convert to float:":
				try:
					print(50)
					replacements[value] = st.number_input(f"Replace '{value}' with:", value=float(value), step=0.01)
				except:
					print(51)
					replacements[value] = st.number_input(f"Replace '{value}' with:", step=0.01)
		# if st.button("Apply :)"):
		if (
			st.button("Apply", on_click=callback)
				or st.session_state.button_clicked
				):
			st.warning(f""""{select}" is applied, but changes will not be saved until you press the 'Confirm Changes' button below.""")
			print(52)
			modified_df = df.copy()
			# Replace categorical values
			print(53)
			modified_df[selected_column].replace(replacements, inplace=True)
			print(54)
			st.write("Modified DataFrame:")
			print(55)
			st.write(modified_df)
			print(56)
			# Explicitly convert the column to the desired data type
			if select == "Convert to int:":
				print(57)
				# modified_df[selected_column] = modified_df[selected_column].astype(int)
				modified_df[selected_column] = modified_df[selected_column].astype(pd.Int64Dtype())
				print(58)
			elif select == "Convert to float:":
				print(59)
				modified_df[selected_column] = modified_df[selected_column].astype(float)

			# Display data type of the modified column
			# st.write(f"Data Type after conversion: :green[{modified_df[selected_column].dtype}]")
			try:
				print(60)
				if modified_df[selected_column].dtype == 'object':
					print(61)
					col1, col2 = st.columns(2)
					with col1:
						print(62)
						unique_values = modified_df[selected_column].nunique()
						print(63)
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						print(64)
						st.write(f"  - Number of Unique Values: :green[{unique_values}]")
						print(65)
						if unique_values <= 20:
							print(66)
							st.write(f"  - Unique Values: :green[{', '.join(map(str, modified_df[selected_column].unique()))}]")
							print(67)
						else:
							print(68)
							st.write(f"  - Top 20 Unique Values:")
							print(69)
							st.write(f":green[{', '.join(map(str, modified_df[selected_column].value_counts().head(20).index))}]")
							print(70)
					with col2:
						print(71)
						plt.figure(figsize=(10, 6))
						try:
							print(72)
							sns.countplot(x=limit_unique_values(modified_df[selected_column]), data=modified_df, color="green")
						except:
							print(73)
							sns.countplot(x=modified_df[selected_column], data=modified_df, color="green")
						plt.xticks(rotation=45)
						st.pyplot()
						plt.close()
						print(74)
					# with st.expander("More Info"):
					# 	print(75)
					# 	tab1, tab2 = st.tabs(["Insights", "Donut chart"])
					# 	with tab1:
					# 		print(76)
					# 		col7, col8, col9 = st.columns(3)
					# 		with col7:
					# 			# Insights
					# 			print(77)
					# 			st.write("## Insights")
					# 			approximate_distinct_count = modified_df[selected_column].nunique()
					# 			approximate_unique_percent = (approximate_distinct_count / len(modified_df)) * 100
					# 			missing = modified_df[selected_column].isna().sum()
					# 			missing_percent = (missing / len(modified_df)) * 100
					# 			memory_size = modified_df[selected_column].memory_usage(deep=True)
					# 			st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
					# 			st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
					# 			st.write(f"Missing: :green[{missing}]")
					# 			st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
					# 			st.write(f"Memory Size: :green[{memory_size}]")
					# 			print(78)

					# 			# st.header("An owl")
					# 			# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
					# 		with col8:
					# 			print(79)
					# 			# Mode and Standard Deviation
					# 			st.write("## Mode")
					# 			# if modified_df[selected_column].dtype == 'object':
					# 			mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
					# 			st.write(f"Mode: :green[{mode}]")
					# 				# st.write("Standard Deviation cannot be calculated for non-numeric data.")
					# 			# else:
					# 				# mode = modified_df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
					# 				# std_dev = modified_df[selected_column].astype(float).std()
					# 				# st.write(f"Mode: {mode}")
					# 				# st.write(f"Standard Deviation: {std_dev}")
					# 		with col9:
					# 			print(80)
					# 			# First 5 Sample Rows
					# 			st.write("## First 5 Sample Rows")
					# 			st.write(modified_df[selected_column].head())

					# 	with tab2:
					# 		print(81)
					# 		# Prepare data for donut chart
					# 		data = limit_unique_values(modified_df[selected_column]).value_counts().reset_index()
					# 		data.columns = [selected_column, 'count']
					# 		print(82)
					# 		fig = px.pie(data, values='count', names=selected_column, hole=0.5)
					# 		fig.update_traces(textposition='inside', textinfo='percent+label')
					# 		fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
					# 		st.plotly_chart(fig)

							# st.header("An owl")
							# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

						
				elif pd.api.types.is_numeric_dtype(modified_df[selected_column]):
					print(83)
					col3, col4 = st.columns(2)
					with col3:
						print(84)
						st.write(f"  - Data Type: :green[{modified_df[selected_column].dtype}]")
						st.write(f"  - Mean: :green[{modified_df[selected_column].mean()}]")
						st.write(f"  - Standard Deviation: :green[{modified_df[selected_column].std():.3}]")
						st.write(f"  - Min Value: :green[{modified_df[selected_column].min()}]")
						st.write(f"  - Max Value: :green[{modified_df[selected_column].max()}]")
					with col4:
						print(85)
						plt.figure(figsize=(10, 6))
						sns.histplot(modified_df[selected_column], kde=True, color="green")
						st.pyplot()
						plt.close()
					# with st.expander("More Info"):
					# 	print(86)
					# 	tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
					# 	with tab1:
					# 		print(87)
					# 		col4, col5, col6 = st.columns(3)
					# 		with col4:
					# 			print(88)
					# 			st.write("#### Basic Statistics")
					# 			insights = calculate_insights(modified_df[selected_column])
					# 			basic_stats = {key: value for key, value in insights.items() if key in [
					# 				'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
					# 			print(89)
					# 			for key, value in basic_stats.items():
					# 				st.write(f"**{key}:** :green[{value:.3f}]")
					# 			print(90)
					# 			st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
					# 			st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
					# 			st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")
					# 			print(91)
					# 		with col5:
					# 			print(92)
					# 			st.write("#### Percentiles")
					# 			descriptive_stats = insights.get('Descriptive statistics')
					# 			print(93)
					# 			if descriptive_stats is not None:
					# 				print(94)
					# 				percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
					# 				if '5%' in descriptive_stats.index:
					# 					percentiles['5%'] = descriptive_stats['5%']
					# 				if '95%' in descriptive_stats.index:
					# 					percentiles['95%'] = descriptive_stats['95%']
					# 				st.write(percentiles)

					# 		with col6:
					# 			print(95)
					# 			st.write("#### Additional Statistics")
					# 			additional_stats = {key: value for key, value in insights.items() if key in [
					# 				'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
					# 			print(96)
					# 			for key, value in additional_stats.items():
					# 				st.write(f"**{key}:** :green[{value:.3f}]")
					# 			# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
					# 			# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
					# 			# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
					# 			# try:
					# 			# 	print(97)
					# 			# 	st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
					# 			# 	print(98)
					# 			# 	st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
					# 			# 	print(99)
					# 			# 	st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
					# 			# 	print(100)
					# 			# except Exception as e:
					# 			# 	print(e)
						
					# 	with tab2:
					# 		print(101)
					# 		try:
					# 			fig = px.box(modified_df, y=selected_column)
					# 		except Exception as e:
					# 			print(e)
					# 		st.plotly_chart(fig)
					# 		print(102)
						
					# 	with tab3:
					# 		print(103)
					# 		plt.figure(figsize=(10, 6))
					# 		print(103)
					# 		qqplot_data = sm.qqplot(modified_df[selected_column], line='s').gca().lines
					# 		print(104)
					# 		try:
					# 			fig = go.Figure()
					# 			fig.add_trace({
					# 				'type': 'scatter',
					# 				'x': qqplot_data[0].get_xdata(),
					# 				'y': qqplot_data[0].get_ydata(),
					# 				'mode': 'markers',
					# 				'marker': {'color': '#19d3f3'}
					# 			})
					# 			fig.add_trace({
					# 				'type': 'scatter',
					# 				'x': qqplot_data[1].get_xdata(),
					# 				'y': qqplot_data[1].get_ydata(),
					# 				'mode': 'lines',
					# 				'line': {'color': '#636efa'}
					# 			})
					# 			x_min = min(qqplot_data[0].get_xdata())
					# 			x_max = max(qqplot_data[0].get_xdata())
					# 			y_min = min(qqplot_data[0].get_ydata())
					# 			y_max = max(qqplot_data[0].get_ydata())
					# 			fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
					# 			fig.update_layout({
					# 				'title': f'QQ Plot for {selected_column}',
					# 				'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
					# 				'yaxis': {'title': 'Sample Quantiles'},
					# 				'showlegend': False,
					# 				'width': 800,
					# 				'height': 700,
					# 			})
					# 			st.plotly_chart(fig)
					# 		except Exception as e:
					# 			print(e)
					

					# 		print(105)
					st.write("---")
					print(106)
				else:
					print(107)
					st.write("DataFrame not found.")
					print(108)
				st.write("``")
				print(109)
				# col11, col22 = st.columns(2)
				# with col11:
				# 	if st.button("Confirm Change"):
				# st.session_state.df = modified_df 
				# 		st.session_state.df = modified_df  # Store modified DataFrame in session state
				# 		st.rerun()

				# with col22:
				# 	# Undo functionality
				# 	# if "modified_df" in st.session_state:
				# 	if st.button("Undo", type='primary'):
				# 		st.rerun()
				# 		# if "copyy" in st.session_state:
				# 		# 	# copyy = st.session_state.copyy
				# 		# 	# st.session_state.df = copyy  # Revert to original DataFrame
				# 		# 	st.session_state.df = st.session_state.copyy
				# 		# 	st.write("Undo successful.")
				# 		# else:
				# 		# 	st.write("hi")
			except ZeroDivisionError:
				print(110)
				pass
			except Exception as e:
				print(111)
				st.error(e)
				st.subheader("⚠️Please upload a file⚠️")
				pass

	# col11, col22 = st.columns(2)
	# with col11:
			confirm_change = st.button('Confirm Change')

			if confirm_change:
				# st.session_state.df = modified_df
				st.session_state.df = modified_df
				# modified_df.to_csv('data3.csv', index=False)
				st.rerun()
except Exception as e:
	print("e:=_", e)
	st.error(e)


	# Update the checkbox value to False after the action
	# st.session_state.confirm_change = False
		

# with col22:
	# Undo functionality
	# if "modified_df" in st.session_state:
# if st.button("Undo", type='primary'):                              # IIMP
# 	st.rerun()
	# if "copyy" in st.session_state:
		# copyy = st.session_state.copyy
		# st.session_state.df = copyy  # Revert to original DataFrame
	# st.session_state.df = ccc
	# st.write("Undo successful.")
	# else:
		# st.write("hi")
	# col11, col22 = st.columns(2)
	# with col11:
	# 	if st.button("Confirm Change"):
	# 		st.session_state.df = modified_df 
	# 		# st.rerun()

	# with col22:
	# 	# Undo functionality
	# 	if "modified_df" in st.session_state:
	# 		if st.button("Undo", type='primary'):
	# 			st.session_state.df = df  # Revert to original DataFrame
	# 			st.write("Undo successful.")



# try:
# 	if df[selected_column].dtype == 'object':
# 		col1, col2 = st.columns(2)
# 		with col1:
# 			unique_values = df[selected_column].nunique()
# 			st.write(f"  - Data Type: :green[{df[selected_column].dtype}]")
# 			st.write(f"  - Number of Unique Values: :green[{unique_values}]")
# 			if unique_values <= 20:
# 				st.write(f"  - Unique Values: :green[{', '.join(map(str, df[selected_column].unique()))}]")
# 			else:
# 				st.write(f"  - Top 20 Unique Values:")
# 				st.write(f":green[{', '.join(map(str, df[selected_column].value_counts().head(20).index))}]")
# 		with col2:
# 			plt.figure(figsize=(10, 6))
# 			try:
# 				sns.countplot(x=limit_unique_values(df[selected_column]), data=df, color="green")
# 			except:
# 				sns.countplot(x=df[selected_column], data=df, color="green")
# 			plt.xticks(rotation=45)
# 			st.pyplot()
# 			plt.close()
# 		with st.expander("More Info"):
# 			tab1, tab2, tab3 = st.tabs(["Insights", "Donut chart", "WordCloud"])
# 			with tab1:
# 				col7, col8, col9 = st.columns(3)
# 				with col7:
# 					# Insights
# 					st.write("## Insights")
# 					approximate_distinct_count = df[selected_column].nunique()
# 					approximate_unique_percent = (approximate_distinct_count / len(df)) * 100
# 					missing = df[selected_column].isna().sum()
# 					missing_percent = (missing / len(df)) * 100
# 					memory_size = df[selected_column].memory_usage(deep=True)
# 					st.write(f"Approximate Distinct Count: :green[{approximate_distinct_count}]")
# 					st.write(f"Approximate Unique (%): :green[{approximate_unique_percent:.2f}%]")
# 					st.write(f"Missing: :green[{missing}]")
# 					st.write(f"Missing (%): :green[{missing_percent:.2f}%]")
# 					st.write(f"Memory Size: :green[{memory_size}]")

# 					# st.header("An owl")
# 					# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
# 				with col8:
# 					# Mode and Standard Deviation
# 					st.write("## Mode")
# 					# if df[selected_column].dtype == 'object':
# 					mode = df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
# 					st.write(f"Mode: :green[{mode}]")
# 						# st.write("Standard Deviation cannot be calculated for non-numeric data.")
# 					# else:
# 						# mode = df[selected_column].mode().iloc[0]  # Mode can return multiple values, taking the first one
# 						# std_dev = df[selected_column].astype(float).std()
# 						# st.write(f"Mode: {mode}")
# 						# st.write(f"Standard Deviation: {std_dev}")
# 				with col9:
# 					# First 5 Sample Rows
# 					st.write("## First 5 Sample Rows")
# 					st.write(df[selected_column].head())

# 			with tab2:
# 				# Prepare data for donut chart
# 				data = limit_unique_values(df[selected_column]).value_counts().reset_index()
# 				data.columns = [selected_column, 'count']

# 				fig = px.pie(data, values='count', names=selected_column, hole=0.5)
# 				fig.update_traces(textposition='inside', textinfo='percent+label')
# 				fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
# 				st.plotly_chart(fig)

# 				# st.header("An owl")
# 				# st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

# 			with tab3:
# 				# Concatenate all values of the column into a single string
# 				cleanstrng = ' '.join(df[selected_column].dropna())

# 				# Check if there are words to plot
# 				if cleanstrng:
# 					# Generate word cloud
# 					word_freq = pd.Series(cleanstrng.split()).value_counts()
					
# 					# Select top 200 words if available, otherwise take the exact number of words
# 					if len(word_freq) >= 50:
# 						top_words = word_freq.head(50)
# 					else:
# 						top_words = word_freq

# 					words_dict = top_words.to_dict()
					
# 					try:
# 						# Generate word cloud from frequencies
# 						wordcloud_ip = WordCloud(background_color='white', width=2800, height=2400).generate_from_frequencies(words_dict)

# 						# Display word cloud
# 						plt.figure(figsize=(10, 7))
# 						plt.imshow(wordcloud_ip, interpolation='bilinear')
# 						plt.title(f'Word Cloud for {selected_column}')
# 						plt.axis('off')
# 						plt.show()
# 						st.pyplot(plt, use_container_width=True)
# 					except Exception as e:
# 						st.write(f"Error generating word cloud: {e}")
# 				else:
# 					st.write(f"No words to plot for column '{selected_column}'")
# 	elif pd.api.types.is_numeric_dtype(df[selected_column]):
# 		col3, col4 = st.columns(2)
# 		with col3:
# 			st.write(f"  - Data Type: :green[{df[selected_column].dtype}]")
# 			st.write(f"  - Mean: :green[{df[selected_column].mean()}]")
# 			st.write(f"  - Standard Deviation: :green[{df[selected_column].std()}]")
# 			st.write(f"  - Min Value: :green[{df[selected_column].min()}]")
# 			st.write(f"  - Max Value: :green[{df[selected_column].max()}]")
# 		with col4:
# 			plt.figure(figsize=(10, 6))
# 			sns.histplot(df[selected_column], kde=True, color="green")
# 			st.pyplot()
# 			plt.close()
# 		with st.expander("More Info"):
# 			tab1, tab2, tab3 = st.tabs(["Insights", "Box plot", "QQ plot"])
# 			with tab1:
# 				col4, col5, col6 = st.columns(3)
# 				with col4:
# 					st.write("#### Basic Statistics")
# 					insights = calculate_insights(df[selected_column])
# 					basic_stats = {key: value for key, value in insights.items() if key in [
# 						'Mean', 'Median', 'Mode', 'Standard deviation', 'Variance', 'Kurtosis', 'Skewness']}
# 					for key, value in basic_stats.items():
# 						st.write(f"**{key}:** :green[{value:.3f}]")
# 					st.write(f"**Memory size:** :green[{insights.get('Memory size', 'N/A'):.3f}]")
# 					st.write(f"**Range:** :green[{insights.get('Range', 'N/A'):.3f}]")
# 					st.write(f"**Interquartile range:** :green[{insights.get('Interquartile range', 'N/A'):.3f}]")

# 				with col5:
# 					st.write("#### Percentiles")
# 					descriptive_stats = insights.get('Descriptive statistics')
# 					if descriptive_stats is not None:
# 						percentiles = descriptive_stats.loc[['min', '25%', '50%', '75%', 'max']]
# 						if '5%' in descriptive_stats.index:
# 							percentiles['5%'] = descriptive_stats['5%']
# 						if '95%' in descriptive_stats.index:
# 							percentiles['95%'] = descriptive_stats['95%']
# 						st.write(percentiles)

# 				with col6:
# 					st.write("#### Additional Statistics")
# 					additional_stats = {key: value for key, value in insights.items() if key in [
# 						'Distinct', 'Distinct (%)', 'Missing', 'Missing (%)', 'Zeros', 'Zeros (%)', 'Negative', 'Negative (%)']}
# 					for key, value in additional_stats.items():
# 						st.write(f"**{key}:** :green[{value:.3f}]")
# 					# st.write(f"**Memory size:** {insights.get('Memory size', 'N/A')}")
# 					# st.write(f"**Range:** {insights.get('Range', 'N/A')}")
# 					# st.write(f"**Interquartile range:** {insights.get('Interquartile range', 'N/A')}")
# 					st.write(f"**Coefficient of variation (CV):** :green[{insights.get('Coefficient of variation (CV)', 'N/A'):.3f}]")
# 					st.write(f"**Median Absolute Deviation (MAD):** :green[{insights.get('Median Absolute Deviation (MAD)', 'N/A'):.3f}]")
# 					st.write(f"**Sum:** :green[{insights.get('Sum', 'N/A'):.3f}]")
# 			with tab2:
# 				fig = px.box(df, y=selected_column)
# 				st.plotly_chart(fig)
# 			with tab3:
# 				plt.figure(figsize=(10, 6))
# 				qqplot_data = sm.qqplot(df[selected_column], line='s').gca().lines
# 				fig = go.Figure()
# 				fig.add_trace({
# 					'type': 'scatter',
# 					'x': qqplot_data[0].get_xdata(),
# 					'y': qqplot_data[0].get_ydata(),
# 					'mode': 'markers',
# 					'marker': {'color': '#19d3f3'}
# 				})
# 				fig.add_trace({
# 					'type': 'scatter',
# 					'x': qqplot_data[1].get_xdata(),
# 					'y': qqplot_data[1].get_ydata(),
# 					'mode': 'lines',
# 					'line': {'color': '#636efa'}
# 				})
# 				x_min = min(qqplot_data[0].get_xdata())
# 				x_max = max(qqplot_data[0].get_xdata())
# 				y_min = min(qqplot_data[0].get_ydata())
# 				y_max = max(qqplot_data[0].get_ydata())
# 				fig.add_trace(go.Scatter(x=[x_min, x_max], y=[y_min, y_max], mode='lines', line=dict(color='red', width=2), name='Identity Line'))
# 				fig.update_layout({
# 					'title': f'QQ Plot for {selected_column}',
# 					'xaxis': {'title': 'Theoretical Quantiles', 'zeroline': False},
# 					'yaxis': {'title': 'Sample Quantiles'},
# 					'showlegend': False,
# 					'width': 800,
# 					'height': 700,
# 				})
# 				st.plotly_chart(fig)
# 		st.write("---")
# 	else:
# 		st.write("DataFrame not found.")
# 	st.write("``")
# except ZeroDivisionError:
# 	pass
# except Exception as e:
# 	st.error(e)
# 	st.subheader("⚠️Please upload a file⚠️")
# 	pass