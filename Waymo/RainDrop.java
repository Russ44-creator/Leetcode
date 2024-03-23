public class RainDrop {
    static class Interval {
        double left = 0, right = 0.01;

        boolean isWet() { 
                return left >= right;
        }
    }

    public static void main(String[] args) {
        simulateRainDrop();
    }

    public static void simulateRainDrop() { 

        Interval[] sidewalk = new Interval[100];
        for (int i = 0; i < 100; i++) {
                sidewalk[i] = new Interval();
        }
        int cnt = 0, wetCnt = 0;
        while (wetCnt < 100) { 
                ++cnt;
                double p = Math.random();
                double left = p - 0.005;
                double right = p + 0.005;
                if (left >= 0) {
                        int idx = (int) (left / 0.01);
                        if (!sidewalk[idx].isWet()) {
                                double iright = left - idx * 0.01;
                                if (iright < sidewalk[idx].right) {
                                        sidewalk[idx].right = iright;
                                        if (sidewalk[idx].isWet())
                                                ++wetCnt;
                                }
                        }
                }
                if (right <= 1) {
                        int idx = (int) (right / 0.01);
                        if (!sidewalk[idx].isWet()) {
                                double ileft = right - idx * 0.01;
                                if (ileft > sidewalk[idx].left) {
                                        sidewalk[idx].left = ileft;
                                        if (sidewalk[idx].isWet())
                                                ++wetCnt;
                                }
                        }
                }
        }
        System.out.println(cnt);
    }
}