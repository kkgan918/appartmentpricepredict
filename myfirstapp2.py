import streamlit as st
import pickle
import numpy as np
import pandas as pd

#dataset source:https://www.kaggle.com/thajegan76/properties-kuala-lumpur-malaysia/data
#reference website 1: https://www.analyticsvidhya.com/blog/2021/11/laptop-price-prediction-practical-understanding-of-machine-learning-project-lifecycle/
#ref website 2:https://github.com/Jcharis/Streamlit_DataScience_Apps/tree/master/EDA_app_with_Streamlit_Components

#load the model and dataframe
df = pd.read_csv('house_price.csv')
pipe = pickle.load(open('house_price.pkl', "rb"))

#Theme


#Sidebar 

# EDA Pkgs
import pandas as pd 
import codecs
from pandas_profiling import ProfileReport 

# Components Pkgs
import streamlit.components.v1 as components
from pandas_profiling import ProfileReport

# analyzing the dataset and displat the report
import sweetviz as sv 
def st_display_sweetviz(report_html,width=1000,height=1000):
                    report_file = codecs.open(report_html,'r')
                    page = report_file.read()
                    components.html(page,width=width,height=height,scrolling=True)
    

footer_temp = """
     <!-- CSS  -->
     <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
     <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
     <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
     <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
     <footer class="page-footer grey darken-4">
     <div class="container" id="aboutapp">
        <div class="row">
            <div class="col l6 s12">
              <h5 class="white-text">Apartment Price Prediction App</h5>
              <p class="grey-text text-lighten-4">Using Streamlit,Pandas and SweetViz.</p>
            </div>
          
       <div class="col l3 s12">
              <h5 class="white-text">Connect With Me</h5>
              <ul>
              <a href="https://gh.linkedin.com/in/kian-kun-gan-4920a1228" target="_blank" class="white-text">
                <i class="fab fa-linkedin fa-4x"></i>
                  </a>
               <a href="https://github.com/kkgan918/" target="_blank" class="white-text">
                <i class="fab fa-github-square fa-4x"></i>
           </a>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-copyright">
          <div class="container">
          Made by <a class="white-text text-lighten-3">Gan Kian Kun</a><br/>
          <a class="white-text text-lighten-3">gankk03@gmail.com</a>
          </div>
        </div>
      </footer>
    """


def main():
    """Finding Your Dream Home?"""

    menu = ["Home","Sweetviz","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Sweetviz":
        st.subheader("Automated EDA with Sweetviz")
        df = pd.read_csv('house_price.csv')
        st.dataframe(data=df, width=1000, height=300)
        if st.button("Generate Sweetviz Report"):

                # Normal Workflow
                report = sv.analyze(df, target_feat="Price")
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")
                            
                
    elif choice == "About":
        st.subheader("About This App")
        # components.iframe('https://jcharistech.com')
        components.html(footer_temp,height=500)

    else:
        #Header
        st.header("Finding Your Dream Home?")
        st.subheader("Let Us Help You")

        components.html("""
            <style>
            * {box-sizing: border-box}
            body {font-family: Verdana, sans-serif; margin:0}
            .mySlides {display: none}
            img {vertical-align: middle;}
            /* Slideshow container */
            .slideshow-container {
              max-width: 1000px;
              position: relative;
              margin: auto;
            }
            /* Next & previous buttons */
            .prev, .next {
              cursor: pointer;
              position: absolute;
              top: 50%;
              width: auto;
              padding: 16px;
              margin-top: -22px;
              color: white;
              font-weight: bold;
              font-size: 18px;
              transition: 0.6s ease;
              border-radius: 0 3px 3px 0;
              user-select: none;
            }
            /* Position the "next button" to the right */
            .next {
              right: 0;
              border-radius: 3px 0 0 3px;
            }
            /* On hover, add a black background color with a little bit see-through */
            .prev:hover, .next:hover {
              background-color: rgba(0,0,0,0.8);
            }
            /*  */
            .text {
              color: #f2f2f2;
              font-size: 15px;
              padding: 8px 12px;
              position: absolute;
              bottom: 8px;
              width: 100%;
              text-align: center;
            }
            /*  */
            .numbertext {
              color: #f2f2f2;
              font-size: 12px;
              padding: 8px 12px;
              position: absolute;
              top: 0;
            }
            /* The dots/bullets/indicators */
            .dot {
              cursor: pointer;
              height: 15px;
              width: 15px;
              margin: 0 2px;
              background-color: #bbb;
              border-radius: 50%;
              display: inline-block;
              transition: background-color 0.6s ease;
            }
            .active, .dot:hover {
              background-color: #717171;
            }
            /* Fading animation */
            .fade {
              -webkit-animation-name: fade;
              -webkit-animation-duration: 1s;
              animation-name: fade;
              animation-duration: 1s;
            }
            @-webkit-keyframes fade {
              from {opacity: .4} 
              to {opacity: 1}
            }
            @keyframes fade {
              from {opacity: .4} 
              to {opacity: 1}
            }
            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {
              .prev, .next,.text {font-size: 11px}
            }
            </style>
            </head>
            <body>
            <div class="slideshow-container">
            <div class="mySlides fade">
              <div class="numbertext">1 / 3</div>
              <img src="https://www.puredestinations.co.uk/wp-content/uploads/2016/06/kuala-lumpur-luxury-holidays-header-1600x500.jpg" style="width:100%">
              <div class="text"> </div>
            </div>
            <div class="mySlides fade">
              <div class="numbertext">2 / 3</div>
              <img src="https://apac-marketing.webbeds.com/wp-content/uploads/2018/08/banyan-header.png" style="width:100%">
              <div class="text"> </div>
            </div>
            <div class="mySlides fade">
              <div class="numbertext">3 / 3</div>
              <img src="https://s7d2.scene7.com/is/image/ritzcarlton/RCR_Kuala_Lumpur_-_Wadding_pool_for_website?$XlargeViewport100pct$" style="width:100%">
              <div class="text">Caption Three</div>
            </div>
            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>
            </div>
            <br>
            <div style="text-align:center">
              <span class="dot" onclick="currentSlide(1)"></span> 
              <span class="dot" onclick="currentSlide(2)"></span> 
            <span class="dot" onclick="currentSlide(3)"></span> 
            </div>
            <script>
            var slideIndex = 1;
            showSlides(slideIndex);
            function plusSlides(n) {
            showSlides(slideIndex += n);
            }
            function currentSlide(n) {
            showSlides(slideIndex = n);
            }
            function showSlides(n) {
              var i;
              var slides = document.getElementsByClassName("mySlides");
              var dots = document.getElementsByClassName("dot");
              if (n > slides.length) {slideIndex = 1}    
              if (n < 1) {slideIndex = slides.length}
              for (i = 0; i < slides.length; i++) {
              slides[i].style.display = "none";  
              }
              for (i = 0; i < dots.length; i++) {
              dots[i].className = dots[i].className.replace(" active", "");
              }
              slides[slideIndex-1].style.display = "block";  
              dots[slideIndex-1].className += " active";
            }
            </script>
             """)
        #Now we will take user input one by one as per our dataframe
        df = pd.read_csv('house_price.csv')
        #Area
        Area = st.selectbox('Location', df['Area'].unique())
        #Bedrooms
        Bedrooms = st.number_input('Bedrooms',min_value=0,key=0)
        #Bathrooms
        Bathrooms = st.number_input('Bathrooms',min_value=0,key=1)
        #sqft
        sqft = st.number_input("Area (in psf)",min_value=300)


        #Prediction
        if st.button("Predict Price ◀", kwargs={
       'clicked_button_ix': 3, 'n_buttons': 4}):
            query = np.array([Area,Bedrooms,Bathrooms,sqft])
            query = query.reshape(1, 4)
            prediction = str(int(np.exp(pipe.predict(query)[0])))
            st.subheader("The predicted price of this apartment is RM" + prediction)




if __name__ == '__main__':
	main()
