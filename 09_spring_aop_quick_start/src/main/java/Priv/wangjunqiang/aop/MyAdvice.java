package Priv.wangjunqiang.aop;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

@Component
// 定义一个切面
@Aspect
public class MyAdvice {
    // 设置切入点
    @Pointcut("execution(void Priv.wangjunqiang.dao.BookDao.update())")
    public void func() {
    }

    @Pointcut("execution(void Priv..save(..))")
    public void func2() {
    }

    // 连接切入点
    // 前置通知
    @Before("func()")
    public void before(JoinPoint joinPoint) {
        // 可以拿到传入的参数
        Object[] args = joinPoint.getArgs();
        System.out.println("Before Aop...");
    }


    // 后置通知
    @After("func()")
    public void after() {
        System.out.println("After Aop...");
    }

    // 环绕通知
    @Around("func2()")
    public Object around(ProceedingJoinPoint proceedingJoinPoint)
        throws Throwable {
        System.out.println("around before");
        Object ret = proceedingJoinPoint.proceed();
        System.out.println("aournd after");
        return ret;
    }

    // 返回后通知
    // 原方法抛异常后不会调用
    @AfterReturning("func()")
    public void afterReturning() {
        System.out.println("afterReturning...");
    }

    // 抛出异常通知
    // 在方法抛出异常时通知
    @AfterThrowing("func()")
    public void afterThrowing() {
        System.out.println("afterThrowing...");
    }
}
