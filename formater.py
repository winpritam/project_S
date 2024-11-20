"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from apikey import key
import json

genai.configure(api_key=key)

# Create the model
generation_config = {
  "temperature": 0.95,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction='',
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
qerry = 'GANPAT UNIVERSITY FACULTY OF COMPUTER APPLICATIONS Programme Master of Computer Applications Branch/Spec. Computer Application Semester II Version 1.0.0.0 Effective from Academic Year 2022-23 Effective for the batch Admitted in June 2022 Subject Code P12A5AIR Subject Name Artificial Intelligence and Robotics Teaching scheme Examination scheme (Marks) (Per week) Lecture (DT) Practical (Lab.) Total CE SEE Total L TU P TW Credit 2 0 2 0 4 Theory 40 60 100 Hours 2 0 4 0 6 Practical 20 30 50 Objective: ● The objective of the course is to basic concepts of artificial intelligence (AI) principles and approaches. ● Develop a basic understanding of the building blocks of AI as presented in terms of intelligent agents: Search, Knowledge representation, inference, logic, and learning. ● To describe the strengths and limitations of various state-space search algorithms, and choose the appropriate algorithm. ● To understand the basic concepts associated with the design and functioning and applications of Robots To study about the drives and sensors used in Robots Pre-requisites: ● Data Structure, Basic probability theory and Statistics, Knowledge of programming language. Course Outcomes : ● 1 = Slight (Low); 2 = Moderate (Medium); 3 = Substantial (High); “-” = No Correlation Name Description of CO CO1 Understand the theory of Artificial intelligence, Intelligent Agents CO2 Learn Prolog Programming language and implement AI algorithm. CO3 Understand Uninformed Search Strategies and apply BFS , DFS and Informed Search Strategies Heuristic Functions, Best-First Search, Greedy Search, A* Algorithm, CO4 To learn about application of Robots, knowledge for the design of robotics, robot kinematics and robot programming, Robotics Actuators, Sensors and Robot Control Mapping of CO and PO Cos PO1 PO2 PO PO4 PO5 PO6 PO7 PO8 PO9 PO10 PO11 PO12 3 CO1 3 3 2 3 3 2 2 2 2 1 1 1 CO2 3 3 3 3 2 2 2 2 2 1 2 -CO3 3 3 2 3 2 2 2 2 3 2 2 2 CO4 2 2 2 2 2 2 2 2 2 3 2 2 Content: Unit Section – I Hrs 1 Introduction to Artificial Intelligence: Brief History, Intelligent Systems, Categorization of 7 Intelligent Systems, Components of AI Program, Foundations of AI, Sub-areas of AI, Applications, Development of AI Languages. Intelligent Agents: Rational Agents, Mapping from Sequences to Actions, Properties of Environments, Structure of Intelligent Agents, Types of Agents: Simple Reflex Agents, Goal Based Agents, Utility Based Agents. 2 Prolog Programming language: Introduction, Prolog Program, Control Strategy of Prolog, 8 Programming Techniques in Prolog, List Manipulation in Prolog, System Predicate, Cut, Effect of Rule and Goal Orders, Structuring of Data in Prolog, Recursive Data Types in Prolog, SystemDefined Predicates. Section – II 3 Uninformed Search Strategies: Breadth-First Search, Uniform Cost Search, Depth-First Search, 8 Analysis of Search Methods, Informed Search Strategies: Heuristic Functions, Best-First Search, Greedy Search, A* Algorithm, Optimal Solution by A* Algorithm. Introduction to Robotics: Classification, Components, Characteristics, Applications. Robotics Kinematics, Position Analysis, Robots as Mechanisms, Matrix Representation, Transformation Matrices, Forward and Inverse Kinematics. 4 Actuators: Characteristics of Actuating Systems, Actuating Devices and Control, Use of Reduction 9 Gears, Comparison Of Hydraulic, Electric, Pneumatic Actuators, Hydraulic Actuators. Sensors: Sensor Characteristics, Description of Different Sensors, Vision Sensors, Force Sensors, Proximity Sensors, Tilt Sensors, Robot Controls: Point to Point Control, Continuous Path Control, Intelligent Robot, Control System for Robot Joint, Control Actions, Feedback Devices. Practical Content: List of programs specified by the subject teacher based on above mentioned topics. Text Books: 1 Artificial Intelligence – A Modern Approach. Second Edition, Stuart Russel, Peter Norvig, PHI, Pearson Education. 2 Prolog Programming for Artificial Intelligence. Ivan Bratka- Third Edition – Pearson Education. 3 Saeed B. Niku, Introduction to Robotics Analysis, Application, Pearson Education Asia, 2001. 4 John J. Craig, “Introduction to Robotics”, 3rd Edition Addison Wesley publication Reference Books: 1 Artificial Intelligence – Structures and Strategies for Complex Problem Solving , George F Luger, Addison Wesley, Fifth Edition 2 Artificial Intelligence, 3rd Edition, Patrick Henry Winston., Pearson Edition. MOOC/Certification Courses: 1 https://onlinecourses.nptel.ac.in/noc22_cs56/preview 2 https://www.edx.org/learn/artificial-intelligence 3 https://in.coursera.org/specializations/ai-foundations-for-everyone Question Paper Scheme: University Examination Duration: 3 Hours Note for Examiner: - (I) Questions 1 and 4 are compulsory with no options. (II) Internal options should be given in questions 2, 3, 5 and 6. SECTION – IQ.1 –8 Marks Q.2 –11 Marks Q.3 –11 Marks SECTION - II Q.4 –8 Marks Q.5 –11 Marks Q.6 –11 Marks'
response = model.generate_content([qerry])
# json_res = json.loads(response.text)
# print(type(response))
print(response.text)
# print(type(json_res))
# print(json_res)


