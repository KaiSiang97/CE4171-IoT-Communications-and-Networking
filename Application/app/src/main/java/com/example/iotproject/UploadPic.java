package com.example.iotproject;

import android.media.Image;

import java.util.List;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.Response;
import okhttp3.ResponseBody;
import retrofit2.Call;

import retrofit2.http.GET;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;
import retrofit2.http.Url;

public interface UploadPic {
    @Multipart
    @POST("/")
    Call<String> uploadPicture(@Part MultipartBody.Part part);

//    @GET("/")
//    Call<List<ImageClass>> getData();
}
