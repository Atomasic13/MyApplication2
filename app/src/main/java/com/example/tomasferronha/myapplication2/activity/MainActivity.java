package com.example.tomasferronha.myapplication2.activity;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.util.SortedList;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.widget.Toast;

import com.example.tomasferronha.myapplication2.R;
import com.example.tomasferronha.myapplication2.adapter.BookAdapter;
import com.example.tomasferronha.myapplication2.model.Book;
import com.example.tomasferronha.myapplication2.model.BookList;
import com.example.tomasferronha.myapplication2.my_interface.GetBookDataService;
import com.example.tomasferronha.myapplication2.network.RetrofitInstance;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private BookAdapter adapter;
    private RecyclerView recyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        /** Create handle for the RetrofitInstance interface*/
        GetBookDataService service = RetrofitInstance.getRetrofitInstance().create(GetBookDataService.class);

        /** Call the method with parameter in the interface to get the Book data*/
        Call<BookList> call = service.getBookData("android");

        /**Log the URL called*/
        Log.d("Test", call.request().url() + "");

        call.enqueue(new Callback<BookList>() {
            @Override
            public void onResponse(Call<BookList> call, Response<BookList> response) {
                Log.d("Test",  " book list");
                generateBookList(response.body().getBookList());
                Log.d("Test", "on REsponse");


            }

            @Override
            public void onFailure(Call<BookList> call, Throwable t) {
                Log.d("Test", "on Failure");
                Toast.makeText(MainActivity.this, "Something went wrong...Error message: " + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }

    /** Method to generate List of Book using RecyclerView with custom adapter*/
    private void generateBookList(ArrayList<Book> BookArrayList) {
        recyclerView = findViewById(R.id.recycler_view_Book_list);
        adapter = new BookAdapter(BookArrayList);
        RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(MainActivity.this);
        recyclerView.setLayoutManager(layoutManager);
        recyclerView.setAdapter(adapter);
    }

}
