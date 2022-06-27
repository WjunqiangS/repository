package Priv.wangjunqiang.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

import java.util.Arrays;

@Component
@Aspect
public class ProjectAdvice {

    @Pointcut("execution(* Priv.wangjunqiang.*.*Service.findBy*(..))")
    private void func() {
    }

    @Around("func()")
    public void runSpeed(ProceedingJoinPoint proceedingJoinPoint)
        throws Throwable {
        long startTime = System.currentTimeMillis();
        for (int i = 0; i < 10000; i++) {
            proceedingJoinPoint.proceed();
        }
        System.out.println("Parameters : " + Arrays.toString(
            proceedingJoinPoint.getArgs()));
        long endTime = System.currentTimeMillis();

        String className =
            proceedingJoinPoint.getSignature().getDeclaringTypeName();

        String name = proceedingJoinPoint.getSignature().getName();

        System.out.println(className + "." +  name + " Cost Time: " + (endTime -
            + startTime) + "ms");
    }
}
