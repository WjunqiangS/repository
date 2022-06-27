package Priv.wangjunqiang.controller;

import Priv.wangjunqiang.exception.BusinessException;
import Priv.wangjunqiang.exception.SystemException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class ExceptionAdvice {
    // 业务层异常处理
    @ExceptionHandler(SystemException.class)
    public Result doSystemException(SystemException e) {

        // 记录日志
        // 通知维护人员
        // 通知开发人员

        // 返回异常结果
        return new Result(e.getCode(), null, e.getMessage());
    }

    // 业务层异常处理
    @ExceptionHandler(BusinessException.class)
    public Result doBusinessException(BusinessException e) {

        // 返回异常结果
        return new Result(e.getCode(), null, e.getMessage());
    }

    // 声明处理未知类型的异常
    @ExceptionHandler(Exception.class)
    public Result doException(Exception e) {
        // 记录日志
        // 通知维护人员
        // 通知开发人员

        // 返回异常结果
        return new Result(ResultCode.SYSTEM_UNKNOWN_EXCEPTION, null,
            "服务器繁忙，请您稍后再试。");
    }
}
