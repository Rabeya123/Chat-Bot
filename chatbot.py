@ -5,21 +5,37 @@ from chatterbot.trainers import ListTrainer
from _tkinter import *
bot=chatterbot.ChatBot(&quot;my bot&quot;)
convo=[
&#39;hello&#39;,
&#39;hey there!&#39;,
&#39;what is your name?&#39;,
&#39;my name is Bot,i am created by rabeya&#39;,
&#39;how are you?&#39;,
&#39;i am doing great these days&#39;,
&#39;thanktyou&#39;,
&#39;In which city you live?&#39;,
&#39;I live in dhaka&#39;,
&#39;In which language you talk?&#39;,
&#39;I most talk in english&#39;
&#39;what is your favourite hobby?&#39;,
&#39;my favourite hobby is playing cricket &#39;,
&#39;what is your profession?&#39;,
&#39;i am student from eastwest university&#39;
&#39;what is coronavirus&#39;,
&#39;Coronaviruses are a large family of viruses which may cause illness in animals or humans&#39;,
&#39;what is COVID-19&#39;,
&#39;COVID-19 is the infectious disease caused by the most recently discovered coronavirus.&#39;,
&#39;what are the symptoms of COVID-19&#39;,
&#39;fever,dry cough,tiredness&#39;,
&#39;who is risk for coronavirus?&#39;,
&#39;these are older people and who are underlying medical condition&#39;
&#39;what should i do if i have COVID-19 symptoms?&#39;,
&#39;stay home,isolate from other,take who guideness&#39;,

&#39;How can we protect others&#39;,
&#39;if possible,maintain minimum 1 meter distance&#39;,
&#39;what should i do if i have close contact with someone who are COVID-19 affected?&#39;
&#39;if you are not live in dengue infected area you can follow minimum 14 days self quarintine yourself &#39;,
&#39;what does mean self-quarantine?&#39;,
&#39;Quarantine means restricting activities or separating people who are not ill themselves&#39;,
&#39;what does mean physical distancing?&#39;,
&#39;minimum 1 meter distance from other&#39;
&#39;what does it mean to self isolate? &#39;,
&#39;keep at least one meter from other and 14 days isolate from other&#39;,
&#39;is there any vaccine drug or treatment?&#39;,
&#39;clean your hand frequently and througly, Avoid touching your nose and mouth, keep minimum 1
meters distance &#39;,
&#39;Does who recommand medical mask for prevenet COVID-19?&#39;,
&#39;WHO recomend N95 and sergical mask for covid-19&#39;,
&#39;how long does the virus survive on surfaces?&#39;,
&#39;COVID-19 virus can survive for up to 72 hours on plastic and stainless steel,&#39;,
&#39;how can protect myself from covid-19?&#39;,
&#39;wash hand minimum 20 second , keep distance minimum 1 meter and use mask&#39;

]
@ -37,7 +53,7 @@ trainer.train(convo)
#print(&quot;bot : &quot;,answer)
main = Tk()
main.geometry(&quot;500x650&quot;)

main.title(&quot;my chatboot&quot;)
main.title(&quot;covid-19 chatbot&quot;)
img=PhotoImage(file=&quot;bot2.png&quot;)
photoL=Label(main,image=img)
photoL.pack(pady=5)
@ -51,7 +67,7 @@ def ask_from_bot():

frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
msgs=Listbox(frame,width=150,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
