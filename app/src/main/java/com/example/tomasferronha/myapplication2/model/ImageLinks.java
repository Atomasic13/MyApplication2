package com.example.tomasferronha.myapplication2.model;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class ImageLinks{
        @SerializedName("smallThumbnail")
        @Expose
        private String smallThumbnail;

    public ImageLinks(String smallThumbnail) {
        this.smallThumbnail = smallThumbnail;
        }

    public String getSmallThumbnail() {
        return smallThumbnail;
    }

    public void setSmallThumbnail(String smallThumbnail) {
        this.smallThumbnail = smallThumbnail;
    }
}
