from flask import Flask, render_template, request, redirect
import mysql.connector 

def add_user(fname, lname, pnum, email):
    query = "INSERT INTO users (fname, lname, pnum, email) VALUES (%s, %s, %s, %s)" 
    values = (fname, lname, pnum, email)

