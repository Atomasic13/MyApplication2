package com.example.tomasferronha.myapplication2.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class VolumeInfo {
    @SerializedName("title")
    @Expose
    private String title;
    @SerializedName("publishedDate")
    @Expose
    private String publishedDate;

    ImageLinks imageLinks;


    public VolumeInfo(String title, String publishedDate, ImageLinks imageLinks) {
        this.title = title;
        this.publishedDate = publishedDate;
        this.imageLinks = imageLinks;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getPublishedDate() {
        return publishedDate;
    }

    public void setPublishedDate(String publishedDate) {
        this.publishedDate = publishedDate;
    }

    public ImageLinks getImageLinks() {
        return imageLinks;
    }

    public void setImageLinks(ImageLinks imageLinks) {
        this.imageLinks = imageLinks;
    }
}
