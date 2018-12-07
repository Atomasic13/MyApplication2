package com.example.tomasferronha.myapplication2.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Book {


    VolumeInfo volumeInfo;
    ImageLinks imageLinks;

    public String getSelfLink() {
        return selfLink;
    }

    public void setSelfLink(String selfLink) {
        this.selfLink = selfLink;
    }

    @SerializedName("selfLink")
    @Expose
    private String selfLink;

    public Book(VolumeInfo volumeInfo, ImageLinks imageLinks) {
        this.volumeInfo = volumeInfo;
        this.imageLinks = imageLinks;
    }

    public VolumeInfo getVolumeInfo() {
        return volumeInfo;
    }

    public void setVolumeInfo(VolumeInfo volumeInfo) {
        this.volumeInfo = volumeInfo;
    }

    public ImageLinks getImageLinks() {
        return imageLinks;
    }

    public void setImageLinks(ImageLinks imageLinks) {
        this.imageLinks = imageLinks;
    }




}
