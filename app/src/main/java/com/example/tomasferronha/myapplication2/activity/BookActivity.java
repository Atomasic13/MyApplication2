package com.example.tomasferronha.myapplication2.activity;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import com.example.tomasferronha.myapplication2.R;

public class BookActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_book);

        Log.d("Test","BookActivity");

        Intent intent = getIntent();
        String id = intent.getStringExtra("selfBook");
        Log.d("Test","intent "+id);
    }
}
