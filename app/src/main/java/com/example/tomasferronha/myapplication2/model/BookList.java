package com.example.tomasferronha.myapplication2.model;

import android.util.Log;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;

public class BookList {

    @SerializedName("items")
    @Expose
    private ArrayList<Book> bookList;


    public ArrayList<Book> getBookList() {
        Log.d("Test",  " book list added");
        return bookList;
    }

    public void setBookList(ArrayList<Book> bookList) {
        this.bookList = bookList;
    }



}
