# CraftHackathon2023_DrKlini

# Introduction 

DrKlini is a mobile application that efficiently assigns patients to medical facilities in Hungary based on their case priority. By seamlessly integrating an AI chatbot and a dynamic booking system, high-priority patients with conditions like pleurisy or acute myocardial infarction (heart attack) receive prompt attention and care.


#  Services

## Medical Chatbot with categorization functionality

LLM chatbots: [link](https://ada.com/) to ADA chatbot

Our application utilizes the powerful ADA chatbot to effectively gather key symptoms from patients and accurately categorize their case as high, medium, or low priority. This categorization plays a crucial role in dispatching patients to the appropriate medical facility at the right time. Following the chatbot conversation, users are provided with self-action recommendations and/or redirected to the booking system. In urgent situations, the system promptly alerts the user to seek emergency medical assistance. 

## Dynamic Booking system

### Data Source ###

The DrKlini project leverages the EESZT database as the primary data source. This eliminates the need for extensive data collection efforts. The application extracts relevant information such as medical records, prescriptions, prospective controls, as well as data pertaining to the distribution of medical equipment and the capacity of healthcare facilities in Hungary. Addtionally, the database encompasses both the public and the private medical sector 

Source : https://e-egeszsegugy.gov.hu/web/eeszt-information-portal/-eeszt-data-provision-step-by-step
> Based on the above, each privately funded healthcare provider holding an operating licence for medical or dental activity has been required to provide data to the EESZT

·       from 1 January 2020 for accession to the EESZT,

·       from 1 June 2020 for meeting the obligation to provide data to the EESZT.

### Dispatching Process ###

We have named the dispatching process "Delta," which operates based on the label output. The label categorization of a patient's case (high, medium, or low priority) determines the appropriate dispatching action. Please refer to the following diagram for an overview of the Delta process:

![Dispatching Process](https://github.com/DorraJaouad/CraftHackathon2023_DrKlini/assets/84044328/173a0362-e6c9-4baa-a47f-5b5ef37a5808)

### Post Booking ###

After a successful booking, we offer an exciting feature to the patient:

Location Guide: [Menetrendek](https://menetrendek.hu/)

This feature provides a convenient location guide for patients. It assists them in finding the necessary information related to schedules, routes, and transportation options.


## Clinical Interaction ##

- Diagnostic Tests 

Once the doctor examines the patient and prescribes an exploration to do , it will be recorded in the patient's record hence rendered on the app.
Patients can book diagnostic tests directly through the application. Additionally, they have the option to review their past diagnostic results. This empowers patients to stay informed about their health status and track their progress.

-  Medical Checkup 
The application provides information on previous medical checkups, including the dates of those checkups. Patients can also view upcoming checkup dates to stay proactive about their healthcare.

## Medical records ##

patients can view additional characteristics such as chronic illnesses, smoking habits, and past bone injuries. This enables patients to have a comprehensive overview of their medical history and make more informed healthcare decisions.

# Current solutions in the market

One of the prominent existing solutions in the market is the [EEESZT](https://www.eeszt.gov.hu/oldalvalaszto.jsp) application. However, DrKlini surpasses EEESZT in several key aspects, making it a superior choice for patients.
Compared to EEESZT, DrKlini provides a more efficient and patient-centric approach to accessing healthcare services, delivering a seamless and responsive experience for individuals in need of medical assistance.

# Future ideas 

The wealth of data captured by the AI model and user interactions within the app presents exciting opportunities for future developments. By aggregating statistics on demand distribution, DrKlini can play a pivotal role in guiding the reallocation of medical amenities across Hungary.
By leveraging the power of data analytics and machine learning, DrKlini can contribute to the improvement of healthcare access and delivery, fostering a more efficient and equitable healthcare system throughout Hungary. 
