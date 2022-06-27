package Priv.wangjunqiang.controller.interceptor;

import org.springframework.stereotype.Component;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Component
public class ProjectInterceptor implements HandlerInterceptor {
    // 在指定controler方法之前执行
    @Override
    public boolean preHandle(HttpServletRequest request,
        HttpServletResponse response, Object handler) throws Exception {
        System.out.println("handler type:" + handler.getClass());
        System.out.println("handler name:" + ((HandlerMethod)handler).getMethod());
        System.out.println("preHandle");
        return true;
    }

    // 在指定controler方法之后执行
    @Override
    public void postHandle(HttpServletRequest request,
        HttpServletResponse response, Object handler, ModelAndView modelAndView)
        throws Exception {
        System.out.println("postHandle");
    }

    // 在postHandle方法之后执行
    @Override
    public void afterCompletion(HttpServletRequest request,
        HttpServletResponse response, Object handler, Exception ex)
        throws Exception {
        System.out.println("afterCompletion");
    }
}
