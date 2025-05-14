import java.util.Scanner;
import java.util.function.Function;

// 时间计算器，计算时分秒
class time {
    public static void FunctionA() {
        int a, b, c, d, e, f;
        int h = 0, m = 0, s = 0;
        Scanner in = new Scanner(System.in);
        System.out.println("请输入时分秒，三个数字中间使用空格分隔");
        a = in.nextInt();
        b = in.nextInt();
        c = in.nextInt();
        System.out.println("请输入终止时分秒，三个数字中间使用空格分隔");
        d = in.nextInt();
        e = in.nextInt();
        f = in.nextInt();
            //计算秒
        if ((c + f) >= 60) {
            s = c + f - 60;
            m = 1;
        } else {
            s = c + f;
        }
        // 计算分
        if ((b + e + m) >= 60) {
            h = 1;
            m += b + e -60;
        } else {
            m += b + e;
        }
        h += a + d;
        System.out.println(h + "小时" + m + "分钟" + s + "秒");

        return;
    }

    public static void FunctionB() {
        int a, b, c, d, e, f;
        int h = 0, m = 0, s = 0;
        Scanner in = new Scanner(System.in);
        System.out.println("请输入时分秒，三个数字中间使用空格分隔");
        a = in.nextInt();
        b = in.nextInt();
        c = in.nextInt();
        System.out.println("请输入终止时分秒，三个数字中间使用空格分隔");
        d = in.nextInt();
        e = in.nextInt();
        f = in.nextInt();

        if ((c - f) < 0) {
            s = 60 + c - f;
            b--;
        } else {
            s = c - f;
        }
        // 计算分
        if ((b - e) < 0) {
            m = 60 + b - e;
            a--;
        } else {
            m = b - e;
        }
        h = a - d;
        System.out.println(h + "小时" + m + "分钟" + s + "秒");

        return;
    }

    public static void main(String[] args) {
        System.out.println("请选择运算方式：1-加 2-减");
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        if (n == 1) {
            FunctionA();
        } else if (n == 2) {
            FunctionB();
        }
    }
}