package Priv.wangjunqiang.controller;

public class ResultCode {

    public static final Integer GET_OK = 20011;
    public static final Integer DELETE_OK = 20021;
    public static final Integer SAVE_OK = 20031;
    public static final Integer UPDATE_OK = 20041;

    public static final Integer GET_ERR = 20010;
    public static final Integer DELETE_ERR = 20020;
    public static final Integer SAVE_ERR = 20030;
    public static final Integer UPDATE_ERR = 20040;

    public static final Integer BUSINESS_EXCEPTION = 40000;
    public static final Integer SYSTEM_EXCEPTION = 50000;
    public static final Integer SYSTEM_UNKNOWN_EXCEPTION = 59999;
}
