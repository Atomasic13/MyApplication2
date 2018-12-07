package com.example.tomasferronha.myapplication2.my_interface;

import com.example.tomasferronha.myapplication2.model.BookList;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface GetBookDataService {

    @GET("volumes?")
    Call<BookList> getBookData(@Query("q") String id );
}
