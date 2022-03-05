### BIT 465 – REST API Development 
### A Complete Django REST API With GitHub Documentations

## Introduction
This assignment is to help you build upon the skills you have acquired from assignment 4 and the first 4 
chapters of Building RESTful Python Web Services. See the submission section for more information 
about what you should submit for this assignment.

## Specification
You  should  build  a  new  API  endpoint  that  allows  an  end  user  to  create  a  new Dog model  by  making 
a POST to /api/dogs,  view  current  dogs  that  have  been  saved  to  the  server  before  by  making  a GET to 
/api/dogs,  and  get,  modify,  or  delete  an  existing Dog record  by  making  a GET, PUT,  or DELETE request 
(respectively)  to /api/dogs/<id> where <id> is  the  id  of  the Dog record  to  be  retrieved,  modified,  or 
deleted.  Since  a Dog includes  a  foreign  key  to  the  breed,  you  also  need  to  make  the  same  type  of 
endpoints for dog breed at /api/breeds/ and /api/breeds/<id>.
  
## Dog model
 A dog should contain the following fields:
  name (a character string)
  age (an integer)
  breed (a foreign key to the Breed Model)
  gender (a character string)
  color (a character string)
  favoritefood (a character string)
  favoritetoy (a character string)
  
## Breed Model
 A breed should contain the following fields:
  name (a character string)
  size (a character string) [should accept Tiny, Small, Medium, Large]
  friendliness (an integer field) [should accept values from 1-5]
  trainability (an integer field) [should accept values from 1-5]
  sheddingamount (an integer field) [should accept values from 1-5]
  exerciseneeds (an integer field) [should accept values from 1-5]
  
## Todo List
To do this, do the following:
  track all your changes using github. 
  add a Dog and Breed models to models.py
  migrate your database to include tables for Dog and Breed
  add two class-based API view controllers for handling Dog REST endpoints to controllers.py
    o call one DogDetail and one DogList to conform to best practice nomenclature
    o The DogDetail class should have three methods named get, put, delete
    o The DogList class should have two methods named get and post
    o refer to Chapter 2 of the recommended text or here for examples
  add two class-based API view controllers for handling Breed REST endpoints to controllers.py
    o call one BreedDetail and one BreedList to conform to best practice nomenclature
    o The BreedDetail class should have three methods named get, put, delete
    o The BreedList class should have two methods named get and post
    o refer to Chapter 2 of the recommended text or here for examples
  add the appropriate url patterns to the urls.py file to accept all the patterns and map them to the correct controller
  test your endpoints with POSTMAN/ web browser (browsable APIs), taking screenshots of each type of request. There should be 5 requests total for each type of model, for a    total of 10 tests and screenshots.
    o GET (list), POST to /api/dogs/
    o GET, PUT, DELETE to /api/dogs/<id>
    o GET (list), POST to /api/breeds/
    o GET, PUT, DELETE to /api/breeds/<id> trainability (an integer field) [should accept values from 1-5]
  sheddingamount (an integer field) [should accept values from 1-5]
  exerciseneeds (an integer field) [should accept values from 1-5]
  
## Todo List
To do this, do the following:
  track all your changes using github. 
  add a Dog and Breed models to models.py
  migrate your database to include tables for Dog and Breed
  add two class-based API view controllers for handling Dog REST endpoints to controllers.py
    o call one DogDetail and one DogList to conform to best practice nomenclature
    o The DogDetail class should have three methods named get, put, delete
    o The DogList class should have two methods named get and post
    o refer to Chapter 2 of the recommended text or here for examples
  add two class-based API view controllers for handling Breed REST endpoints to controllers.py
    o call one BreedDetail and one BreedList to conform to best practice nomenclature
    o The BreedDetail class should have three methods named get, put, delete
    o The BreedList class should have two methods named get and post
    o refer to Chapter 2 of the recommended text or here for examples
  add the appropriate url patterns to the urls.py file to accept all the patterns and map them to the correct controller
  test your endpoints with POSTMAN/ web browser (browsable APIs), taking screenshots of each type of request. There should be 5 requests total for each type of model, for a total of 10 tests and screenshots.
    o GET (list), POST to /api/dogs/
    o GET, PUT, DELETE to /api/dogs/<id>
    o GET (list), POST to /api/breeds/
