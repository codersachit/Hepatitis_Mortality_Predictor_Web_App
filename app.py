# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 


# Utils
import os
import joblib 
import hashlib

from PIL import Image


# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')


# DB
import sqlite3
conn = sqlite3.connect('usersdata.db')
c = conn.cursor()

# Functions

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data



def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def generate_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()


def verify_hashes(password,hashed_text):
	if generate_hashes(password) == hashed_text:
		return hashed_text
	return False

feature_names_best = ['age', 'sex', 'steroid', 'antivirals', 'fatigue', 'spiders', 'ascites','varices', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime','histology']

gender_dict = {"male":1,"female":2}
feature_dict = {"No":1,"Yes":2} 


def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 

def get_key(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return key

def get_fvalue(val):
	feature_dict = {"No":1,"Yes":2}
	for key,value in feature_dict.items():
		if val == key:
			return value 

# Load ML Models
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model



html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Hepatitis B Mortality Prediction </h1>
		</div>
		"""

# Avatar Image using a url
#avatar1 ="https://www.w3schools.com/howto/img_avatar1.png"
#avatar2 ="https://www.w3schools.com/howto/img_avatar2.png"

result_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>	
	<p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
	</div>
	"""

result_temp2 ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
	<img src="https://www.w3schools.com/howto/{}" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>	
	<p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
	</div>
	"""

prescriptive_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">Recommended Life style modification</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
		<li style="text-align:justify;color:black;padding:10px">Get Plenty of Rest</li>
		<li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
		<li style="text-align:justify;color:black;padding:10px">Avoid Alchol</li>
		<li style="text-align:justify;color:black;padding:10px">Proper diet</li>
		<ul>
		<h3 style="text-align:justify;color:black;padding:10px">Medical Mgmt</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Consult your doctor</li>
		<li style="text-align:justify;color:black;padding:10px">Take your interferons</li>
		<li style="text-align:justify;color:black;padding:10px">Go for checkups</li>
		<ul>
	</div>
	"""


ques = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h2 style="color:white;text-align:center;">What is Hepatitis B ?</h2>
		</div>
		"""	



descriptive_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">Definition</h3>
		<p>Hepatitis B is a viral infection that attacks the liver and can cause both acute and chronic disease.</p>
	</div>
	"""
page_bg_img = '''
<style>
body {
background-image: url("https://www.cdc.gov/hepatitis/statistics/2018surveillance/images/HumanFigureWithLiver.jpg");
background-size: cover;
}
</style>
'''

about_message ="""
	
		<h3 style="text-align:justify;color:black;padding:10px">Important Information</h3>
		<p><h1>Overview</h1>
Hepatitis B is a serious liver infection caused by the hepatitis B virus (HBV). For some people, hepatitis B infection becomes chronic, meaning it lasts more than six months. Having chronic hepatitis B increases your risk of developing liver failure, liver cancer or cirrhosis — a condition that permanently scars of the liver.
Most adults with hepatitis B recover fully, even if their signs and symptoms are severe. Infants and children are more likely to develop a chronic (long-lasting) hepatitis B infection.
A vaccine can prevent hepatitis B, but there's no cure if you have the condition. If you're infected, taking certain precautions can help prevent spreading the virus to others.
<img src="https://5qyy93evuhggy2io39kk451b-wpengine.netdna-ssl.com/wp-content/uploads/sites/12/2019/10/liver_hepatitisB_1055490376-860x574.jpg"  width="700" height="500">
 <h2>Symptoms</h2><p>Signs and symptoms of hepatitis B range from mild to severe. They usually appear about one to four months after you've been infected, although you could see them as early as two weeks post-infection. Some people, usually young children, may not have any symptoms.</p>
<p>Hepatitis B signs and symptoms may include:</p>
<ul>
    <li>Abdominal pain</li>
    <li>Dark urine</li>
    <li>Fever</li>
    <li>Joint pain</li>
    <li>Loss of appetite</li>
    <li>Nausea and vomiting</li>
    <li>Weakness and fatigue</li>
    <li>Yellowing of your skin and the whites of your eyes (jaundice)</li>
</ul>
<img src="https://reportshealthcare.com/wp-content/uploads/2017/10/Hepatitis-C-Treatments-Give-Patients-More-Options.jpg" width="700" height="500">
 <h3>When to see a doctor</h3><p>If you know you've been exposed to hepatitis B, contact your doctor immediately. A preventive treatment may reduce your risk of infection if you receive the treatment within 24 hours of exposure to the virus.</p>
<p>If you think you have signs or symptoms of hepatitis B, contact your doctor.</p>
        
<h2>Causes</h2>
<p>Hepatitis B infection is caused by the hepatitis B virus (HBV). The virus is passed from person to person through blood, semen or other body fluids. It does not spread by sneezing or coughing.</p>
<p>Common ways that <abbr title="hepatitis B virus">HBV</abbr> can spread are:</p>
<ul>
    <li><strong>Sexual contact.</strong> You may get hepatitis B if you have unprotected sex with someone who is infected. The virus can pass to you if the person's blood, saliva, semen or vaginal secretions enter your body.</li>
    <li><strong>Sharing of needles.</strong> <abbr title="Hepatitis B virus">HBV</abbr> easily spreads through needles and syringes contaminated with infected blood. Sharing IV drug paraphernalia puts you at high risk of hepatitis B.</li>
    <li><strong>Accidental needle sticks.</strong> Hepatitis B is a concern for health care workers and anyone else who comes in contact with human blood.</li>
    <li><strong>Mother to child.</strong> Pregnant women infected with <abbr title="hepatitis B virus">HBV</abbr> can pass the virus to their babies during childbirth. However, the newborn can be vaccinated to avoid getting infected in almost all cases. Talk to your doctor about being tested for hepatitis B if you are pregnant or want to become pregnant.</li>
</ul>
<h3>Acute vs. chronic hepatitis B</h3><p>Hepatitis B infection may be either short-lived (acute) or long lasting (chronic).</p>
<ul>
    <li><strong>Acute hepatitis B infection</strong> lasts less than six months. Your immune system likely can clear acute hepatitis B from your body, and you should recover completely within a few months. Most people who get hepatitis B as adults have an acute infection, but it can lead to chronic infection.</li>
    <li><strong>Chronic hepatitis B infection</strong> lasts six months or longer. It lingers because your immune system can't fight off the infection. Chronic hepatitis B infection may last a lifetime, possibly leading to serious illnesses such as cirrhosis and liver cancer.</li>
</ul>
<p>The younger you are when you get hepatitis B &mdash; particularly newborns or children younger than 5 &mdash; the higher your risk of the infection becoming chronic. Chronic infection may go undetected for decades until a person becomes seriously ill from liver disease.</p>
        
<h2>Risk factors</h2><p>Hepatitis B spreads through contact with blood, semen or other body fluids from an infected person. Your risk of hepatitis B infection increases if you:</p>
<ul>
    <li>Have unprotected sex with multiple sex partners or with someone who's infected with <abbr title="hepatitis B virus">HBV</abbr></li>
    <li>Share needles during IV drug use</li>
    <li>Are a man who has sex with other men</li>
    <li>Live with someone who has a chronic <abbr title="hepatitis B virus">HBV</abbr> infection</li>
    <li>Are an infant born to an infected mother</li>
    <li>Have a job that exposes you to human blood</li>
    <li>Travel to regions with high infection rates of <abbr title="hepatitis B virus">HBV</abbr>, such as Asia, the Pacific Islands, Africa and Eastern Europe</li>
</ul>
        
            
<h2>Complications</h2><p>Having a chronic <abbr title="hepatitis B virus">HBV</abbr> infection can lead to serious complications, such as:</p>
<ul>
    <li><strong>Scarring of the liver (cirrhosis).</strong> The inflammation associated with a hepatitis B infection can lead to extensive liver scarring (cirrhosis), which may impair the liver's ability to function.</li>
    <li><strong>Liver cancer.</strong> People with chronic hepatitis B infection have an increased risk of liver cancer.</li>
    <li><strong>Liver failure.</strong> Acute liver failure is a condition in which the vital functions of the liver shut down. When that occurs, a liver transplant is necessary to sustain life.</li>
    <li><strong>Other conditions.</strong> People with chronic hepatitis B may develop kidney disease or inflammation of blood vessels.</li>
</ul>
        
            
<h2>Prevention</h2><p>The hepatitis B vaccine is typically given as three or four injections over six months. You can't get hepatitis B from the vaccine.</p>
<img src="https://i0.wp.com/cdn-prod.medicalnewstoday.com/content/images/articles/324/324208/nurse-giving-a-hepatitis-b-vaccine.jpg?w=1155&h=1541" width="700" height="500">
<p>The hepatitis B vaccine is recommended for:</p>
<ul>
    <li>Newborns</li>
    <li>Children and adolescents not vaccinated at birth</li>
    <li>Those who work or live in a center for people who are developmentally disabled</li>
    <li>People who live with someone who has hepatitis B</li>
    <li>Health care workers, emergency workers and other people who come into contact with blood</li>
    <li>Anyone who has a sexually transmitted infection, including HIV</li>
    <li>Men who have sex with men</li>
    <li>People who have multiple sexual partners</li>
    <li>Sexual partners of someone who has hepatitis B</li>
    <li>People who inject illegal drugs or share needles and syringes</li>
    <li>People with chronic liver disease</li>
    <li>People with end-stage kidney disease</li>
    <li>Travelers planning to go to an area of the world with a high hepatitis B infection rate</li>
</ul>
        
            
<h3>Take precautions to avoid HBV</h3><p>Other ways to reduce your risk of <abbr title="hepatitis B virus">HBV</abbr> include:</p>
<ul>
    <li><strong>Know the <abbr title="hepatitis B virus">HBV</abbr> status of any sexual partner.</strong> Don't engage in unprotected sex unless you're absolutely certain your partner isn't infected with <abbr title="hepatitis B virus">HBV</abbr> or any other sexually transmitted infection.</li>
    <li><strong>Use a new latex or polyurethane condom every time you have sex</strong> if you don't know the health status of your partner. Remember that although condoms can reduce your risk of contracting <abbr title="hepatitis B virus">HBV</abbr>, they don't eliminate the risk.</li>
    <li><strong>Don't use illegal drugs.</strong> If you use illicit drugs, get help to stop. If you can't stop, use a sterile needle each time you inject illicit drugs. Never share needles.</li>
    <li><strong>Be cautious about body piercing and tattooing.</strong> If you get a piercing or tattoo, look for a reputable shop. Ask about how the equipment is cleaned. Make sure the employees use sterile needles. If you can't get answers, look for another shop.</li>
    <li><strong>Ask about the hepatitis B vaccine before you travel.</strong> If you're traveling to a region where hepatitis B is common, ask your doctor about the hepatitis B vaccine in advance. It's usually given in a series of three injections over a six-month period.</li>
</ul>            
<h1>Intererting Facts</h1>
<img src="https://cdn.nanalyze.com/uploads/2019/03/Hepatitis-B-Generic-Hepatitis-Drugs.png" width="700" height="500">
	"""

about_temp="""
<h1>Application Built By:</h1>
<ul>
<li>Ritvik Mahajan: GCET/71/17 (Computer Engg.)</li>
<li>Sachit: GCET/49/17 (Computer Engg.)</li>
<li>Rohit Raina: GCET/214/17 (Computer Engg.)</li>
</ul>
"""


def main():
	st.markdown(html_temp.format('royalblue'),unsafe_allow_html=True)


	menu = ["Home","Login","SignUp","Facts","About"]
	submenu = ["Prediction","Plot"]


	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.markdown(ques.format('blue'),unsafe_allow_html=True)

		
		st.markdown(descriptive_message_temp,unsafe_allow_html=True)

		st.markdown(page_bg_img, unsafe_allow_html=True)


	elif choice == "SignUp":

		new_username = st.text_input("User name")
		new_password = st.text_input("Password", type='password')

		confirm_password = st.text_input("Confirm Password",type='password')

		if new_password == confirm_password:
			st.success("Password Confirmed")
		else:
			st.warning("Passwords not the same")

		if st.button("Submit"):
			create_usertable()
			hashed_new_password = generate_hashes(new_password)
			add_userdata(new_username,hashed_new_password)
			st.success("You have successfully created a new account")
			st.info("Login to Get Started")



	elif choice =='Facts':
		st.markdown(about_message,unsafe_allow_html=True)

	elif choice =='About' :
		st.markdown(about_temp,unsafe_allow_html=True)



		
			



	elif choice == "Login":

		username = st.sidebar.text_input("Username")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			create_usertable()
			hashed_pswd = generate_hashes(password)
			result = login_user(username,verify_hashes(password,hashed_pswd))
			# if password == "12345":
			if result:
				st.success("Welcome {}".format(username))
				activity = st.selectbox("Activity",submenu)
				if activity == "Plot":
					st.subheader("Data Visualisation Plot")
					df = pd.read_csv("data/clean_hepatitis_dataset.csv")
					st.dataframe(df)
					

					df['class'].value_counts().plot(kind='bar')
					st.pyplot()

					# Freq Dist Plot
					freq_df = pd.read_csv("data/freq_df_hepatitis_dataset.csv")
					st.bar_chart(freq_df['count'])


					if st.checkbox("Area Chart"):
						all_columns = df.columns.to_list()
						feat_choices = st.multiselect("Choose a Feature",all_columns)
						new_df = df[feat_choices]
						st.area_chart(new_df)
						



				elif activity == "Prediction":
					st.subheader("Predictive Analytics")
				

					age = st.number_input("Age",7,80)
					sex = st.radio("Sex",tuple(gender_dict.keys()))
					steroid = st.radio("Do You Take Steroids?",tuple(feature_dict.keys()))
					antivirals = st.radio("Do You Take Antivirals?",tuple(feature_dict.keys()))
					fatigue = st.radio("Do You Have Fatigue",tuple(feature_dict.keys()))
					spiders = st.radio("Presence of Spider Naeve",tuple(feature_dict.keys()))
					ascites = st.selectbox("Ascities",tuple(feature_dict.keys()))
					varices = st.selectbox("Presence of Varices",tuple(feature_dict.keys()))
					bilirubin = st.number_input("bilirubin Content",0.0,8.0)
					alk_phosphate = st.number_input("Alkaline Phosphate Content",0.0,296.0)
					sgot = st.number_input("Sgot",0.0,648.0)
					albumin = st.number_input("Albumin",0.0,6.4)
					protime = st.number_input("Prothrombin Time",0.0,100.0)
					histology = st.selectbox("Histology",tuple(feature_dict.keys()))
					feature_list = [age,get_value(sex,gender_dict),get_fvalue(steroid),get_fvalue(antivirals),get_fvalue(fatigue),get_fvalue(spiders),get_fvalue(ascites),get_fvalue(varices),bilirubin,alk_phosphate,sgot,albumin,int(protime),get_fvalue(histology)]
					st.write(len(feature_list))
					st.write(feature_list)
					pretty_result = {"age":age,"sex":sex,"steroid":steroid,"antivirals":antivirals,"fatigue":fatigue,"spiders":spiders,"ascites":ascites,"varices":varices,"bilirubin":bilirubin,"alk_phosphate":alk_phosphate,"sgot":sgot,"albumin":albumin,"protime":protime,"histolog":histology}
					st.json(pretty_result)
					single_sample = np.array(feature_list).reshape(1,-1)

					# ML
					model_choice = st.selectbox("Select Model",["LR","KNN","DecisionTree"])
					if st.button("Predict"):
						if model_choice == "KNN":
							loaded_model = load_model("models/knn_model.pkl")
							prediction = loaded_model.predict(single_sample)
							pred_prob = loaded_model.predict_proba(single_sample)
						elif model_choice == "DecisionTree":
							loaded_model = load_model("models/decision_tree_model.pkl")
							prediction = loaded_model.predict(single_sample)
							pred_prob = loaded_model.predict_proba(single_sample)
						else:
							loaded_model = load_model("models/logistic_regression_model.pkl")
							prediction = loaded_model.predict(single_sample)
							pred_prob = loaded_model.predict_proba(single_sample)

						# st.write(prediction)
						# prediction_label = {"Die":1,"Live":2}
						# final_result = get_key(prediction,prediction_label)
						#if prediction == 1:
						#	st.warning("Patient Dies")
						#	pred_probability_score = {"Die":pred_prob[0][0]*100,"Live":pred_prob[0][1]*100}
						#	st.subheader("Prediction Probability Score using {}".format(model_choice))
						#	st.json(pred_probability_score)
						#	st.subheader("Prescriptive Analytics")
						#	st.markdown(prescriptive_message_temp,unsafe_allow_html=True)
							
						#else:
						#	st.success("Patient Lives")
						#	pred_probability_score = {"Die":pred_prob[0][0]*100,"Live":pred_prob[0][1]*100}
						#	st.subheader("Prediction Probability Score using {}".format(model_choice))
						#	st.json(pred_probability_score)
							

			else:
				st.warning("Incorrect Username/Password")	

	
if __name__=='__main__':
	main()
