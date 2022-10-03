# Advanced BIM - Assignment 1 Group 2
Members: Nicklas Mikkelsen and Anders Træland

## Use case: Cost Estimation of structural materials

We have chosen the Use Case "Cost Estimation" with special emphasis on structural elements and materials. The aim for this assignment is to predict quantity, cost and price for the structural and bearing elements of a project. Based on this information a stakeholder might decide whether or not to proceed with a project, and see how profitable it might be. 

## What does our script try to identify?

We wanted to dive into the structural aspects of the IFC-file. By doing this we want to make a use case for contractors and subcontrctors so that they can estimate the quantities and properties of the structural elements in the IFC. By doing this the Use Case makes it possible to estimate the cost and automatically provide a price in the early stages of the project. This will give the contractors an indication about whether or not its profitable to continue with the tender competition. The idea is that the Use Case will provide simple and understandable structural details and dimensions. Contractors can use these values to implement their own costs, based on type of material, construction time, transportation, equipment etc.  

## How does our script address this problem?

Our plan is to make a script in order to analyze material quantities and dimensions in any project by using IFCOpenShell. Our current script focuses on doors and windows in order to calculate the dimensions of the recess in concrete/bricks. By calculating the area of the recess, the contractor can decide whether it should be drilled after the concrete hardens, or built in as framework. The script defines a condition which can later be changed by the operator. Originally this condition says that if the recess is smaller than 0.5m^2 it should be drilled after hardening. As the assignment goes on, this script will develop and look at much more aspects of the IFC file. 

## What disciplinary expertise have we used to solve this case? 

During our Bachelor's degree we both had internships for construction contractors. During these periods we learned and understood the great amount of materials it takes to complete a project. We believe there is need for a simple and interdisciplinary tool in order to calculate the different amounts and costs. It is important that this tool is quick and effective, and that it can be used on any given project. If a contractor can find the exact amounts of a given material or element, it will make logistics easier, optimize the cost and reduce excess material. In the end this will also lead to a more sustainable production. For this assignment we have used our basic and throughout knowledge about concrete, steel and building practices in order to come up with a Use Case that can hopefully benefit the industry. 

## What IFC concepts have we used in our scripts? 

We have mainly focused on IfcObjectDefinition and IfcPropertyDefinition in order to extract the values for the different elements in the model. This is done in order to define which objects we want to analyze and use their properties to satisfy our use case. 

## What disciplinary analyis does it require? 

Cost and value analysis, as well as some structural analysis with emphasis on quantity and quality of materials. 

## What building elements are we interested in? 

Our disciplin within engineering is the structural part of it, and we are therefore mainly interested in the cost of structural and bearing elements of a building. This includes beams, columns, walls, slabs etc. This is the Use Case we will have the most advantage of in our future careers, and we want to make a useful and effective Use Case for these building elements. 

## What use cases must be done before we can start our use case? 

There has to be a detailed structural and architectural model. There is also need for the indoor and energy use case with regards to ventilation. 

## What is the input data for our use case?

Price per unit of quantity and quality. 

## What other use cases are waiting for ours to be completed? 

Build/operate