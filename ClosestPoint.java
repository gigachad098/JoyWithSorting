import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeMap;
import java.lang.Math;

public class ClosestPoint {
    public static void main(final String[] args) throws FileNotFoundException {
        final Scanner input = new Scanner(System.in);
        ArrayList<Point> pointList = new ArrayList<>();
        while (input.hasNextLine()) {
            String[] temp = input.nextLine().split(" ");
            pointList.add(new Point(Double.parseDouble(temp[0]), Double.parseDouble(temp[1])));
        }
        pointList.sort(new PointXComparator());
        double d = Integer.MAX_VALUE;
        int jcount = 0;
        if (pointList.size() <= 1) {
            d = 0;
        }
        else {
            int pointiindex = 0;
            int pointjindex = jcount++;
            d = computeDist(pointList.get(pointiindex), pointList.get(pointjindex));
            TreeMap<Point, Integer> map = new TreeMap<>(new PointYComparator());
            map.put(pointList.get(pointiindex), pointiindex);
            map.put(pointList.get(pointjindex), pointjindex);
            while (pointjindex <= pointList.size() - 1) {
                for (int i = pointiindex; i < pointjindex; i++) {
                    if (pointList.get(pointjindex).x - pointList.get(i).x < d) {
                        map.put(pointList.get(i), i);
                    }
                }
                Point mapfirstentry = map.firstKey();
                Point maplastentry = map.lastKey();
                while (!mapfirstentry.equals(maplastentry)) {
                    if (computeDist(mapfirstentry, maplastentry) < d) {
                        d = computeDist(mapfirstentry, maplastentry);
                    }
                    mapfirstentry = map.higherEntry(mapfirstentry).getKey();
                }
                while (pointList.get(pointjindex).x - pointList.get(pointiindex).x <= d) {
                    int newjindex = pointjindex++;
                    int newiindex = pointiindex++;
                    if (pointList.get(newjindex).x - pointList.get(newiindex).x <= d) {
                        map.remove(pointList.get(pointjindex));
                        map.remove(pointList.get(pointiindex));
                        pointjindex = newjindex;
                        pointiindex = newiindex;
                    }
                }
            }
        }
        System.out.println("The closest pair of points is " + d);
    }
    public static double computeDist(Point a, Point b) {
        return Math.sqrt(Math.pow((b.x - a.x), 2) + Math.pow((b.y - a.y), 2));
    }
}
