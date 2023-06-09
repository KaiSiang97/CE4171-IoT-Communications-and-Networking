package com.example.iotproject;

import okhttp3.OkHttpClient;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.converter.scalars.ScalarsConverterFactory;

public class NetworkClient {
    private static Retrofit retrofit;
    private static final String BASE_URL = "http://192.168.43.215:8080";

    public static Retrofit getRetrofit() {
        OkHttpClient okHttpClient = new OkHttpClient.Builder().build();
        if (retrofit == null) {
//            retrofit = new Retrofit.Builder().baseUrl(BASE_URL).addConverterFactory(GsonConverterFactory.create()).client(okHttpClient).build();
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
//                    .addConverterFactory(GsonConverterFactory.create())
                    .addConverterFactory(ScalarsConverterFactory.create())
                    .client(okHttpClient)
                    .build();
        }
        return retrofit;
    }
}
