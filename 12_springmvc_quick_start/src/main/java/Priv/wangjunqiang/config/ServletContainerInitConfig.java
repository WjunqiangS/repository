package Priv.wangjunqiang.config;

import org.springframework.web.context.WebApplicationContext;
import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;
import org.springframework.web.servlet.support.AbstractAnnotationConfigDispatcherServletInitializer;
import org.springframework.web.servlet.support.AbstractDispatcherServletInitializer;


public class ServletContainerInitConfig extends
    AbstractAnnotationConfigDispatcherServletInitializer {
    @Override
    protected Class<?>[] getRootConfigClasses() {
        return new Class[]{SpringConfig.class};
    }

    @Override
    protected Class<?>[] getServletConfigClasses() {
        return new Class[]{SpringMVCConfig.class};
    }

    @Override
    protected String[] getServletMappings() {
        return new String[]{"/"};
    }
}


// public class ServletContainerInitConfig extends
//     AbstractDispatcherServletInitializer {
//
//     @Override
//     // servlet配置
//     protected WebApplicationContext createServletApplicationContext() {
//         // 创建SpringMVC容器
//         AnnotationConfigWebApplicationContext configWebApplicationContext =
//             new AnnotationConfigWebApplicationContext();
//
//         configWebApplicationContext.register(SpringMVCConfig.class);
//
//         return configWebApplicationContext;
//     }
//
//     // Servlet拦截所有路径
//     @Override
//     protected String[] getServletMappings() {
//         return new String[]{"/"};
//     }
//
//     @Override
//     // Spring配置
//     protected WebApplicationContext createRootApplicationContext() {
//         // 创建Spring容器
//         AnnotationConfigWebApplicationContext configWebApplicationContext =
//             new AnnotationConfigWebApplicationContext();
//
//         configWebApplicationContext.register(SpringConfig.class);
//
//         return configWebApplicationContext;
//     }
// }
