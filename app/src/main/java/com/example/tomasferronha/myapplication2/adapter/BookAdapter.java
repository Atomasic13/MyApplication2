package com.example.tomasferronha.myapplication2.adapter;

import android.content.Context;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.support.annotation.NonNull;
import android.support.v7.widget.CardView;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.tomasferronha.myapplication2.R;
import com.example.tomasferronha.myapplication2.activity.BookActivity;
import com.example.tomasferronha.myapplication2.model.Book;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;


public class BookAdapter extends RecyclerView.Adapter<BookAdapter.BookViewHolder> {

    private Context context;

    private ArrayList<Book> dataList;

    public BookAdapter(ArrayList<Book> dataList) {
        this.dataList = dataList;
    }

    @NonNull
    @Override
    public BookViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());
        View view = layoutInflater.inflate(R.layout.single_view_row, parent, false);
        return new BookViewHolder(view);

    }

    @Override
    public void onBindViewHolder(BookViewHolder holder, final int position) {
        Log.d("Test","On Bind View« Holder");
        holder.txtBookTitle.setText(dataList.get(position).getVolumeInfo().getTitle());
        holder.txtBookBrief.setText(dataList.get(position).getVolumeInfo().getPublishedDate());
        DownloadImageWithURLTask downloadTask = new DownloadImageWithURLTask(holder.imgView);
        downloadTask.execute(dataList.get(position).getVolumeInfo().getImageLinks().getSmallThumbnail());
        holder.txtImgURL.setText(dataList.get(position).getVolumeInfo().getImageLinks().getSmallThumbnail());
        holder.bookLine.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {
                Intent i = new Intent(context.getApplicationContext(),BookActivity.class);
               // i.putExtra("selfBook",dataList.get(position).g etVolumeInfo().getTitle());
                context.getApplicationContext().startActivity(i);


            }
        });

    }

    @Override
    public int getItemCount() {
        return dataList.size();
    }

    class BookViewHolder extends RecyclerView.ViewHolder {

        TextView txtBookTitle, txtBookBrief, txtImgURL;
        ImageView imgView;
        Button bookLine;

        BookViewHolder(View itemView) {
            super(itemView);
            txtBookTitle = itemView.findViewById(R.id.txt_Book_title);
            txtBookBrief = itemView.findViewById(R.id.txt_Book_brief);
            txtImgURL = itemView.findViewById(R.id.txt_Book_file_path);
            imgView = itemView.findViewById(R.id.imageView);
            bookLine = itemView.findViewById(R.id.button);

        }

    }

    private class DownloadImageWithURLTask extends AsyncTask<String, Void, Bitmap> {
        ImageView bmImage;
        public DownloadImageWithURLTask(ImageView bmImage) {
            this.bmImage = bmImage;
        }

        protected Bitmap doInBackground(String... urls) {
            String pathToFile = urls[0];
            Bitmap bitmap = null;
            try {
                InputStream in = new java.net.URL(pathToFile).openStream();
                bitmap = BitmapFactory.decodeStream(in);
            } catch (Exception e) {
                Log.e("Error", e.getMessage());
                e.printStackTrace();
            }
            return bitmap;
        }
        protected void onPostExecute(Bitmap result) {
            bmImage.setImageBitmap(result);
        }
    }




}
